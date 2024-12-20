# -*- coding: utf-8 -*-
""" CAI41046108 ML Engineering --- utils.py
"""


import json
import re
import os
import time

import numpy as np


## os / paths
def ensure_exists(dir_fp):
    if not os.path.exists(dir_fp):
        os.makedirs(dir_fp)


## parsing / string conversion to int / float
def is_int(s):
    try:
        z = int(s)
        return z
    except ValueError:
        return None


def is_number(s):
    try:
        z = int(s)
        return z
    except ValueError:
        try:
            z = float(s)
            return z
        except ValueError:
            return None


def train_test_val_split(x, y, prop_vec, shuffle=True, seed=None):

    assert x.shape[0] == y.shape[0]
    prop_vec = prop_vec / np.sum(prop_vec) # normalize

    n = x.shape[0]
    n_train = int(np.ceil(n * prop_vec[0]))
    n_test = int(np.ceil(n * prop_vec[1]))
    n_val = n - n_train - n_test

    assert np.amin([n_train, n_test, n_val]) >= 1   

    if shuffle:
        rng = np.random.default_rng(seed)
        pi = rng.permutation(n)
    else:
        pi = xrange(0, n)

    pi_train = pi[0:n_train]
    pi_test = pi[n_train:n_train+n_test]
    pi_val = pi[n_train+n_test:n]

    train_x = x[pi_train]
    train_y = y[pi_train]

    test_x = x[pi_test]
    test_y = y[pi_test]

    val_x = x[pi_val]
    val_y = y[pi_val]  
    
    return train_x, train_y, test_x, test_y, val_x, val_y


def print_array_hist(x, label=None):
    assert len(x.shape) <= 1 or x.shape[1] == 1

    if label is not None:
        print('--- {} ---'.format(label))
    for v in np.unique(x):
        print('{}: {}'.format(v, np.sum(x == v)))



def print_array_basic_stats(x, label=None):
    assert len(x.shape) <= 1 or x.shape[1] == 1

    if label is not None:
        print('--- {} ---'.format(label))

    print('min: {:.2f}'.format(np.amin(x)))
    print('max: {:.2f}'.format(np.max(x)))
    print('mean (+- std): {:.2f} (+- {:.2f})'.format(np.mean(x), np.std(x)))      
        

"""
## Load and preprocess the MNIST dataset
"""
def load_preprocess_mnist_data(flatten=True, onehot=True, prop_vec=[26, 2, 2], seed=None, verbose=False):

    from tensorflow.keras.datasets import mnist
    import tensorflow.keras as keras
    
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    if verbose: # MNIST has overall shape (60000, 28, 28) --- 60k images, each is 28 x 28 pixels
        print('Loaded MNIST data; shape: {} [y: {}], test shape: {} [y: {}]'.format(x_train.shape, y_train.shape,
                                                                                      x_test.shape, y_test.shape))
    
    if flatten: # Let's flatten the images for easier processing (labels don't change)
        flat_vec_size = 28*28
        x_train = x_train.reshape(x_train.shape[0], flat_vec_size)
        x_test = x_test.reshape(x_test.shape[0], flat_vec_size)

    if onehot: # Put the labels in "one-hot" encoding using keras' to_categorical()
        num_classes = 10
        y_train = keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)

    # let's aggregate all the data then split
    all_x = np.r_[x_train, x_test]
    all_y = np.r_[y_train, y_test]
    
    # split the data into train, test, val
    train_x, train_y, test_x, test_y, val_x, val_y = train_test_val_split(all_x, all_y, prop_vec, shuffle=True, seed=seed)
    
    return train_x, train_y, test_x, test_y, val_x, val_y, all_x, all_y
