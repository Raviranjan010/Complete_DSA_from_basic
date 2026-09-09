/* 
Given an array of integers 'a', move all the even integers at the
beginning of the array followed by all the odd integers. The
relative order of odd or even integers does not matter. Return
any array that satisfies the condition.
*/

#include <iostream>
#include <vector>
using namespace std;

void sortByParity(vector<int> &v) {
    int left = 0, right = v.size() - 1;

    while (left < right) {
        // If left is odd and right is even, swap
        if (v[left] % 2 != 0 && v[right] % 2 == 0) {
            swap(v[left], v[right]);
            left++;
            right--;
        }
        // If left is even, just move forward
        if (v[left] % 2 == 0) left++;
        // If right is odd, just move backward
        if (v[right] % 2 != 0) right--;
    }
}

int main() {
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;

    vector<int> v(n);
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    sortByParity(v);

    cout << "Array after sorting by parity: ";
    for (int i = 0; i < n; i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    return  0;
}
