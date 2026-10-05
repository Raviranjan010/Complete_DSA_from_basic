#include <iostream>
#include <vector>
#include <climits> // Needed for INT_MIN

using namespace std;

int secondLargest(const vector<int>& arr) {
    int largest = INT_MIN, secondLargest = INT_MIN;

    for (int num : arr) {
        if (num > largest) {
            secondLargest = largest;
            largest = num;
        } else if (num > secondLargest && num < largest) {
            secondLargest = num;
        }
    }
 
    // If secondLargest was never updated, return INT_MIN
    return (secondLargest == INT_MIN) ? -1 : secondLargest;
}

int main() {
    vector<int> arr = {10, 20, 30, 40, 50, 60, 70, 80, 90};
    int result = secondLargest(arr);

    if (result == -1) {
        cout << "No second largest element found." << endl;
    } else {
        cout << "The second largest element is: " << result << endl;
    }

    return 0;
}
