/*Given an array of integers 'a', move all the even integers at the
beginning of the array followed by all the odd integers. The
relative order of odd or even integers does not matter. Return
any array that satisfies the condition.*/
#include <iostream>
#include <vector>
using namespace std;
void moveEvenToFront(vector<int> &a) {
    int n = a.size();
    vector<int> even, odd;

    // Separate even and odd numbers
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) {
            even.push_back(a[i]);
        } else {
            odd.push_back(a[i]);
        }
    }

    // Combine even and odd numbers
    a.clear();
    a.insert(a.end(), even.begin(), even.end());
    a.insert(a.end(), odd.begin(), odd.end());
}
int main() {
    vector<int> a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    cout << "Original array: ";
    for (int num : a) {
        cout << num << " ";
    }
    cout << endl;

    moveEvenToFront(a);

    cout << "Array after moving even integers to the front: ";
    for (int num : a) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
// Output:
