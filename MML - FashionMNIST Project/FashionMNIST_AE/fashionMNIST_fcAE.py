#!/usr/bin/env python
# coding: utf-8

from utils import mnist_reader
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

X_train, y_train = mnist_reader.load_mnist('data/fashion', kind='train')
X_test, y_test = mnist_reader.load_mnist('data/fashion', kind='t10k')

X_train = np.float32(X_train)
X_test = np.float32(X_test)

x_std = np.std(X_train)
x_mean = np.mean(X_train)

class Autoencoder(nn.Module):
    def __init__(self, input_dim = 784, latent = 8):
        super().__init__()
        
        self.enc1 = nn.Linear(in_features=input_dim, out_features=input_dim//2)
        self.enc2 = nn.Linear(in_features=input_dim//2, out_features=input_dim//4)
        self.enc3 = nn.Linear(in_features=input_dim//4, out_features=latent)
        
        self.dec1 = nn.Linear(in_features=latent, out_features=input_dim//4)
        self.dec2 = nn.Linear(in_features=input_dim//4, out_features=input_dim//2)
        self.dec3 = nn.Linear(in_features=input_dim//2, out_features=input_dim)
    
    def encode(self, x):
        x = self.enc1(x)
        x = nn.LeakyReLU(0.5)(x)
        x = self.enc2(x)
        x = nn.LeakyReLU(0.5)(x)
        x = self.enc3(x)
        x = nn.LeakyReLU(0.5)(x)
        return x
    
    def decode(self, x):        
        x = self.dec1(x)
        x = nn.LeakyReLU(0.5)(x)
        x = self.dec2(x)
        x = nn.LeakyReLU(0.5)(x)
        x = self.dec3(x)
        return x

    def forward(self, x):
        latent = self.encode(x)
        recon = self.decode(latent)
        return recon

x_train= torch.from_numpy(X_train)
x_test = torch.from_numpy(X_test)

# Perform same scaling on training and test datasets
x_train_std = (x_train-torch.mean(x_train))/torch.std(x_train)
x_test_std = (x_test-torch.mean(x_train))/torch.std(x_train)
x_train_std_max = x_train_std.max()
x_train_std_min = x_train_std.min()
x_train_std_norm = (x_train_std - x_train_std_min)/(x_train_std_max-x_train_std_min)
x_test_std_norm = (x_test_std - x_train_std_min)/(x_train_std_max-x_train_std_min)
    
latent_dim = 8
model = Autoencoder(latent=latent_dim)
model.load_state_dict(torch.load('./results/latent_{}_best_parameters_std_norm.pt'.format(latent_dim)))

with torch.no_grad():
    result_train = model(x_train_std_norm).detach().cpu()
    result_test = model(x_test_std_norm).detach().cpu()
    
    h_train = model.encode(x_train_std_norm)
    h_test = model.encode(x_test_std_norm)
    output_from_h_train = model.decode(h_train).detach().cpu()
    output_from_h_test = model.decode(h_test).detach().cpu()
    
    # Reverse the decoder process
    
    # Activation function is LeakyReLU(0.5)(x)
    # Inverse is x=x when x>=0 and x=0.5x otherwise
    activation_inv = lambda x: torch.where(x >= 0, x, 2*x)
    
    # Start with decoder-fc3
    weight = model.dec3.weight # shape is (784, 392)
    bias = model.dec3.bias # shape is (784)
    
    # Reverse self.dec3(x)
    # forward process was x = (x @ weight.T) + bias
    # so we need to subtract bias and multiply by inverse of W.T
    dec3_input_train = (x_train_std_norm - bias) @ torch.linalg.pinv(weight.T)
    dec3_input_test = (x_test_std_norm - bias) @ torch.linalg.pinv(weight.T)
    
    # Reverse nn.LeakyReLU(0.5)(x)
    dec2_output_train = activation_inv(dec3_input_train)
    dec2_output_test = activation_inv(dec3_input_test)
    
    # Reverse self.dec2(x)
    weight = model.dec2.weight
    bias = model.dec2.bias
    dec2_input_train = (dec2_output_train - bias) @ torch.linalg.pinv(weight.T)
    dec2_input_test = (dec2_output_test - bias) @ torch.linalg.pinv(weight.T)
    
    # Reverse nn.LeakyReLU(0.5)(x)
    dec1_output_train = activation_inv(dec2_input_train)
    dec1_output_test = activation_inv(dec2_input_test)
    
    # Reverse self.dec1(x)
    weight = model.dec1.weight
    bias = model.dec1.bias.cpu()
    dec1_input_train = (dec1_output_train - bias) @ torch.linalg.pinv(weight.T)
    dec1_input_test = (dec1_output_test - bias) @ torch.linalg.pinv(weight.T)
    
    h_train_from_output = dec1_input_train 
    h_test_from_output = dec1_input_test
    
    print("Frobenius norm between latent space discovered by Autoencoder and least-squares approach with true instances:")
    print("training set=", 
          torch.norm(h_train-h_train_from_output))
    print("test set=", 
          torch.norm(h_test-h_test_from_output))
    
    output_from_true_h_train = model.decode(h_train_from_output)
    output_from_true_h_test = model.decode(h_test_from_output)
    
    print("\nFrobenius norm at top layer between ouputs and targets:")
    print("training set=", 
          torch.norm(output_from_h_train-output_from_true_h_train))
    print("test set=", 
          torch.norm(output_from_h_test-output_from_true_h_test))
    

# =============================================================================
#     plt.figure()
#     plt.imshow(x_test[0].reshape([28, 28]))
#     plt.figure()
#     plt.imshow(output_from_h_test[0].reshape([28, 28]))
#     plt.figure()
#     plt.imshow(output_from_true_h_test[0].reshape([28, 28]))
# =============================================================================

