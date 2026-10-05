// Program to print the first k multiples of a given number 'num' using recursion.
// Constraints: k > 0
// Example 1:
// Input: num = 12, k = 5
// Output: 12 24 36 48 60
// Example 2:
// Input: num = 3, k = 8
// Output: 3 6 9 12 15 18 21 24

#include <iostream>
using namespace std;

// Function to print the first k multiples of 'num' recursively
void printMultiples(int num, int k) {
    if (k == 0) return; // Base case: stop when k reaches 0
    printMultiples(num, k - 1); // Recursive call for previous multiples
    cout << (num * k) << " ";   // Print the k-th multiple
}

int main() {
    int num, k;
    cout << "Enter the number (num): ";
    cin >> num;
    cout << "Enter how many multiples to print (k): ";
    cin >> k;

    if (k <= 0) {
        cout << "k must be greater than 0." << endl;
        return 1;
    }

    cout << "First " << k << " multiples of " << num << ": ";
    printMultiples(num, k);
    cout << endl;
    return 0;
}