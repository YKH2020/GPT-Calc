#include <iostream>
#include <string>
#include <queue>
#include <sstream>
using namespace std;

// Student Object
struct Student {
    int height = 1; // Default Height is One
    string name, id; // Strings for Name and ID

    // Student Constructor that initializes Student with v and s, which are id and name
    Student(string v, string s) : id(std::move(v)), name(std::move(s)), left(nullptr), right(nullptr) {}

    // Left and Right Pointers
    Student* left;
    Student* right;
};

class AVL {
    // STL Queues
    queue<Student*> q;
    queue<string> q2;

    // Checking whether certain functions are successful or unsuccessful
    bool success = false;

    // Private Functions
    static Student* rotateLeft(Student* root);
    static Student* rotateRight(Student* root);
    static Student* minValueNode(Student* root);
    static int getHeight(Student* root);
    static int getBalance(Student* root);

    // Public Functions
public:
    Student* insert(string& name, string& id, Student* student, Student* &root);
    Student* remove(Student* &root, string &id);
    void searchIDtoNAME(string& id, Student* root);
    void searchNAMEtoID(string& name, Student* root);
    void removeInOrderN(Student* root);
    void inOrder(Student* root);
    void preOrder(Student* root);
    void postOrder(Student* root);
    int levelCount(Student* root);

    Student* removeInorderFinal(Student* &root, int &N);
    static bool checkInt(const string& temp);
    static bool checkString(const string& temp);
    bool getSuccess() const;
    void setSuccess(bool set);
};

// Mini Algorithms

// Locates index through queue to use in remove function
Student* AVL::removeInorderFinal(Student* &root, int &N) {
    int n = 0;
    if (N+1 > q2.size()) {
        while(!q2.empty()) q2.pop();
        return root;
    }
    while(n < N) {
        q2.pop();
        n++;
    }
    Student* temp = remove(root, q2.front());
    while(!q2.empty()) q2.pop();
    return temp;
}

// Iterates through the inorder successor to reach its minimum value (Based on Exam/TA Reviews)
Student* AVL::minValueNode(Student* root) {
    while (root && root->left != nullptr) root = root->left;
    return root;
}

// Rotate Left and Right
Student* AVL::rotateLeft(Student* root) {
    Student* nP = root->right;
    Student* gC = nP->left;
    nP->left = root;
    root->right = gC;
    return nP;
}

Student* AVL::rotateRight(Student* root) {
    Student* nP = root->left;
    Student* gC = nP->right;
    nP->right = root;
    root->left = gC;
    return nP;
}

// Returns the Height of the Student* root
int AVL::getHeight(Student* root) {
    if (root == nullptr) return 0;
    return root->height;
}

// Similar to getHeight, subtracting left-right to get a number for choosing rotations
int AVL::getBalance(Student* root) {
    if (root == nullptr) return 0;
    return getHeight(root->left) - getHeight(root->right);
}

// Checks if the temp string is an Integer
bool AVL::checkInt(const string& temp) {
    int digitTally = 0;

    for (char i : temp) {
        if(isdigit(i) != 0) digitTally++;
    }

    return digitTally == temp.size();
}

// Checks if the temp string is a String
bool AVL::checkString(const string& temp) {
    for (char i : temp) {
        if (isalpha(i) == 0 && isblank(i) == 0)
            return false;
    }
    return true;
}

// Getter and Setter for Success Boolean (used to check if successful or unsuccessful operation)
bool AVL::getSuccess() const {
    return success;
}

void AVL::setSuccess(bool set) {
    success = set;
}

// Main Algorithms

// Inserts a new Student node as a root
Student* AVL::insert(string &name, string &id, Student* student, Student* &root) {
    // Inserts like a normal BST (Based on Exam/TA Reviews)
    if (root == nullptr) {
        cout << "successful\n";
        return student;
    }
    else if(id < root->id)
        root->left = insert(name, id, student, root->left);
    else if(id > root->id)
        root->right = insert(name, id, student, root->right);
    else if (student->id == root->id)
        cout << "unsuccessful\n";

    // AVL Balancing (Getting the Parent Node relative to the child's position)
    // Concept in Lecture Vid (1 plus maximum of left child's and right child's height for parent)
    if (getHeight(root->left) > getHeight(root->right)) root->height = 1 + getHeight(root->left);
    else root->height = 1 + getHeight(root->right);

    // (Balancing with the root with the height inserted into)
    int bal = getBalance(root);

    // Checks if greater than or less than 1 and -1, then rotations happen (Starts at 2 or -2)
    // If only at 2 or -2 (Based on table in lecture vid) then it would only execute for the first imbalance
    // Left Left & Left Right
    if (bal > 1) {
        if (getBalance(root->left) >= 0) return rotateRight(root);
        if (getBalance(root->left) < 0) {
            root->left = rotateLeft(root->left);
            return rotateRight(root);
        }
    }

    // Right Right & Right Left
    if (bal < -1) {
        if (getBalance(root->right) <= 0) return rotateLeft(root);
        if (getBalance(root->right) > 0) {
            root->right = rotateRight(root->right);
            return rotateLeft(root);
        }
    }
    return root;
}

// Removes a Student node as a root
Student* AVL::remove(Student* &root, string &id) {
    // Removes like a normal BST (Based on Exam/TA Reviews)
    if (root == nullptr) {
        success = false;
        return root;
    }
    if (id < root->id)
        root->left = remove(root->left, id);
    else if (id > root->id)
        root->right = remove(root->right, id);

    else {
        success = true;
        if (root->left == nullptr) {
            Student* temp = root->right;
            delete root;
            return temp;
        }
        else if (root->right == nullptr) {
            Student* temp = root->left;
            delete root;
            return temp;
        }

        Student* temp = minValueNode(root->right);

        root->name = temp->name;
        root->id = temp->id;

        root->right = remove(root->right, temp->id);

    }

    // AVL Balancing (Based on Insert above)
    if (getHeight(root->left) > getHeight(root->right)) root->height = 1 + getHeight(root->left);
    else root->height = 1 + getHeight(root->right);

    int bal = getBalance(root);

    // Best is get the balance factor and see if children can be rotated to get new relative parent node
    // Left Left & Left Right
    if (bal > 1) {
        if (getBalance(root->left) >= 0) return rotateRight(root);
        if (getBalance(root->left) < 0) {
            root->left = rotateLeft(root->left);
            return rotateRight(root);
        }
    }

    // Right Right & Right Left
    if (bal < -1) {
        if (getBalance(root->right) <= 0) return rotateLeft(root);
        if (getBalance(root->right) > 0) {
            root->right = rotateRight(root->right);
            return rotateLeft(root);
        }
    }

    return root;
}

// Using a depth first search to find the name of person from id, vice versa
void AVL::searchIDtoNAME(string &id, Student* root) {
    if (root == nullptr)
        return;
    if (id == root->id) {
        cout << root->name << "\n";
        success = true;
    }
    else if (id < root->id && root->left != nullptr)
        searchIDtoNAME(id, root->left);
    else if (id > root->id && root->right != nullptr)
        searchIDtoNAME(id, root->right);
}

void AVL::searchNAMEtoID(string &name, Student* root) {
    if (root == nullptr)
        return;
    else {
        if (name == root->name) {
            cout << root->id << "\n";
            success = true;
        }
        if (root->left != nullptr)
            searchNAMEtoID(name, root->left);
        if (root->right != nullptr)
            searchNAMEtoID(name, root->right);
    }
}

// Pushes Student* onto queue for easier access later on
void AVL::removeInOrderN(Student* root) {
    if (root == nullptr)
        return;
    else {
        removeInOrderN(root->left);
        q2.push(root->id);
        removeInOrderN(root->right);
    }
}

// All the Depth first traversals
void AVL::inOrder(Student *root) {
    if (root == nullptr)
        return;
    else {
        inOrder(root->left);
        if(root->left) cout << ", ";
        cout << root->name;
        if(root->right) cout << ", ";
        inOrder(root->right);
    }
}

void AVL::postOrder(Student *root) {
    if (root == nullptr)
        return;
    else {
        postOrder(root->left);
        if(root->left) cout << ", ";
        postOrder(root->right);
        if(root->right) cout << ", ";
        cout << root->name;
    }
}

void AVL::preOrder(Student *root) {
    if (root == nullptr)
        return;
    else {
        cout << root->name;
        if(root->left) cout << ", ";
        preOrder(root->left);
        if(root->right) cout << ", ";
        preOrder(root->right);
    }
}

// Prints out the height of the tree, essentially using queues
int AVL::levelCount(Student *root) {
    // Data
    int lvlSum = 0, compare = 0;
    bool firstTurn = false;

    // Comparison
    q.push(root);
    unsigned int count = q.size();

    while (!q.empty()) {
        root = q.front();
        compare++;

        if (compare == count) {
            if (firstTurn) lvlSum++;
            compare = 0;
            firstTurn = true;
        }

        if (compare == 0) count = q.size();

        if (root != nullptr) {
            q.push(root->left);
            q.push(root->right);
        }
        q.pop();
    }
    return lvlSum;
}


int main() {
    // # of commands to be entered
    int numTurns;

    // Variables
    string sentence;
    string name;
    string id;
    vector<string> sentences;

    // Core Objects
    AVL avl;
    Student* root = nullptr;

    // Reading the Commands
    getline(cin, sentence);
    numTurns = stoi(sentence);

    // Pushes into vector so it can be processed all in one block in the input
    for (int i = 0; i < numTurns; i++) {
        getline(cin, sentence);
        sentences.push_back(sentence);
    }

    // Performs the function calls for the output of each of these commands
    for (int i = 0; i < sentences.size(); i++) {
        if (sentences[i].find("insert") != string::npos) {
            name = sentences[i].substr(8, sentences[i].size()-18);

            string tempID = sentences[i].substr(sentences[i].size()-8, 8);
            id = tempID;

            if (id.size() == 8 && avl.checkInt(id) && avl.checkString(name)) {
                auto *student = new Student(id, name);
                root = avl.insert(name, id, student, root);
            }
            else
                cout << "unsuccessful\n";
        }
        if (sentences[i].find("remove ") != string::npos) {
            string tempID = sentences[i].substr(7, 8);
            id = tempID;

            if (id.size() == 8)
                root = avl.remove(root, id);

            if (avl.getSuccess()) cout << "successful\n";
            else cout << "unsuccessful\n";
            avl.setSuccess(false);
        }
        if (sentences[i].find("search") != string::npos) {
            string temp = sentences[i].substr(7, sentences[i].size()-7);

            if(avl.checkInt(temp)) {
                id = temp;
                if (id.size() == 8)
                    avl.searchIDtoNAME(id, root);
            }
            else {
                name = temp.substr(1,temp.size()-2);
                if (avl.checkString(name))
                    avl.searchNAMEtoID(name, root);
            }
            if (!avl.getSuccess()) cout << "unsuccessful\n";
            avl.setSuccess(false);
        }
        if (sentences[i].find("removeInorder") != string::npos) {
            string tempID = sentences[i].substr(14, sentences[i].size()-14);
            int N = stoi(tempID);

            avl.removeInOrderN(root);
            root = avl.removeInorderFinal(root, N);

            if (avl.getSuccess()) cout << "successful\n";
            else cout << "unsuccessful\n";
            avl.setSuccess(false);
        }
        if (sentences[i] == "printInorder") {
            avl.inOrder(root);
            cout << "\n";
        }
        if (sentences[i] == "printPreorder") {
            avl.preOrder(root);
            cout << "\n";
        }
        if (sentences[i] == "printPostorder") {
            avl.postOrder(root);
            cout << "\n";
        }
        if (sentences[i] == "printLevelCount")
            cout << avl.levelCount(root) << "\n";
    }
    return 0;
}
