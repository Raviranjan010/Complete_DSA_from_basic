// Demonstration of std::unordered_map and std::unordered_set in C++
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int main() {
    vector<int> nums = {4, 2, 2, 8, 3, 3, 1};
    unordered_map<int, int> freq;
    for (int x : nums) {
        freq[x]++;
    }

    cout << "Element frequencies:" << endl;
    for (auto& pair : freq) {
        cout << pair.first << " -> " << pair.second << endl;
    }

    unordered_set<int> unique_elements(nums.begin(), nums.end());
    cout << "Unique count: " << unique_elements.size() << endl;

    return 0;
}
