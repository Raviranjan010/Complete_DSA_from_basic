#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

// Recursive function to find the minimum cost for the frog to reach the last stone
int frogJump(int n, const vector<int>& height, int i) {
    // Base case: If the frog is already on the last stone, no cost is needed
    if (i == n - 1) return 0;

    // If the frog can only jump to the last stone
    if (i == n - 2)
        return abs(height[i] - height[i + 1]);

    // The frog can jump to the next stone or skip one stone
    int jumpOne = frogJump(n, height, i + 1) + abs(height[i] - height[i + 1]);
    int jumpTwo = frogJump(n, height, i + 2) + abs(height[i] - height[i + 2]);

    // Return the minimum cost of the two possible jumps
    return min(jumpOne, jumpTwo);
}

int main() {
    vector<int> heights = {30, 40, 20, 10};
    int n = heights.size();

    cout << "Minimum cost to reach stone " << n << ": "
         << frogJump(n, heights, 0) << endl;

    return 0;
}