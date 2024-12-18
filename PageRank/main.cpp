#include<iostream>
#include<iomanip>
#include<sstream>
#include<vector>
#include<map>
#include<unordered_map>
#include<string>
using namespace std;

class AdjacencyList {
private:
    //This Unordered Map is used for storing the adjacency list. (Key: Website, Value: Vector of Adjacent Websites)
    unordered_map<string, vector<string>> m;

    // This map is the final map that is outputted, pairs are used for easier calculation with power iterations.
    map<string, pair<double, double>> mFinal;
public:
    void insert(string from, string to); //(1) Inserts two websites that are adjacent into mFinal and m.
    bool isEdge(string from, string to); //(2) Tests whether two websites are connected in the graph.
    vector<string> getAdjacent(string to); //(3) Returns a vector of all websites that are directed to website "to".
    void PageRank(int power); //(4) Responsible for printing out mFinal after "power" amount of power iterations.
};

void AdjacencyList::insert(string from, string to) { //(1)
    // Inserts a Website (from) and what website it points to (to).
    m[from].push_back(to);

    // Makes sure all websites are identified, default initialization of the pair is zero.
    mFinal[from] = make_pair(0, 0);
    mFinal[to] = make_pair(0, 0);

}

bool AdjacencyList::isEdge(string from, string to) { //(2)
    //Returns a boolean indicating true or false, if Websites "from" and "to" are connected.
    for (int i = 0; i < m[from].size(); i++) if (m[from][i] == to) return true;
    return false;
}

vector<string> AdjacencyList::getAdjacent(string to) { //(3)
    vector<string> temp;

    if (mFinal.find(to) == mFinal.end())
        return {};

    // Uses isEdge() to determine whether the key value is connected to "to" in map m, then adds to a vector.
    for (auto iter = m.begin(); iter != m.end(); iter++) {
        if (isEdge(iter->first, to))
            temp.push_back(iter->first);
    }

    return temp;
}

void AdjacencyList::PageRank(int power) { //(4)
    double N = mFinal.size(); // Number of vertices in the graph being used in first power iteration.
    for (int i = 0; i < power; i++) {
        // Copies all values from second value in pair to first, after a power iteration.
        for (auto tempIter = mFinal.begin(); tempIter != mFinal.end(); tempIter++)
            mFinal[tempIter->first].first = mFinal[tempIter->first].second;

        // Iterator traverses the mFinal map.
        for (auto iter = mFinal.begin(); iter != mFinal.end(); iter++) {
            if (i == 0)
                mFinal[iter->first].second = 1 / N;

            if (power == 1)
                break;

            // The following gets the adjacent values as a vector, uses the size as the out degree.
            // Then, it calculates after the first power iteration using the saved pairs in mFinal.
            if (i > 0) {
                vector<string> out = getAdjacent(iter->first);
                if (out.empty())
                    mFinal[iter->first].second = 0;

                else {
                    for (int j = 0; j < out.size(); j++) {
                        double outDeg = m[out[j]].size();
                        if (j == 0)
                            mFinal[iter->first].second = mFinal[out[j]].first / outDeg;

                        if (j > 0)
                            mFinal[iter->first].second += mFinal[out[j]].first / outDeg;
                    }
                }
            }

        }
    }

    // Final print out of all of the websites.
    for (auto iter = mFinal.begin(); iter != mFinal.end(); iter++)
        cout << iter->first << " " << fixed << setprecision(2) << mFinal[iter->first].second << endl;

}

int main() {
    int no_of_lines, power_iterations;
    std::string from, to;
    std::cin >> no_of_lines;
    std::cin >> power_iterations;

    //Create an adjacency list object.
    AdjacencyList Created_Graph;

    for(int i=0;i< no_of_lines;i++) {
        std::cin>>from;
        std::cin>>to;
        // Insertion of each website.
        Created_Graph.insert(from, to);
    }

    // Calls PageRank function for calculations using power iterations and successive printing.
    Created_Graph.PageRank(power_iterations);
}