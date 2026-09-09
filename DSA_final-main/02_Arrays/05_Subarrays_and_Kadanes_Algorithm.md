# Subarrays and Kadane's Algorithm in C++ ➕

## 1️⃣ Understanding Subarrays

A subarray is a contiguous part of an array. For an array of size `n`, there are `n(n+1)/2` non-empty subarrays. This guide explores how to generate subarrays and calculate their sums efficiently.

### Printing All Subarrays

To print all subarrays of a given array, you can use nested loops. The outer loop determines the starting point of the subarray, and the inner loop determines the ending point.

```cpp
#include <iostream>
using namespace std;

void printSubarray(int *arr, int n) {
    for (int start = 0; start < n; start++) {
        for (int end = start; end < n; end++) {
            cout << "(" << start << "," << end << ")" << "->";
            for (int i = start; i <= end; i++) {
                cout << arr[i] << " ";
            }
            cout << endl;
        }
    }
}

int main() {
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr) / sizeof(int);
    printSubarray(arr, n);
    return 0;
}
```

### Calculating Subarray Sums

To calculate the sum of each subarray, you can add another loop inside the nested loops to sum the elements of each subarray.

```cpp
#include <iostream>
#include <climits>
using namespace std;

void maxSubArraySum(int* arr, int n) {
    int maxSum = INT_MIN;
    for (int start = 0; start < n; start++) {
        for (int end = start; end < n; end++) {
            int currSum = 0;
            for (int i = start; i <= end; i++) {
                currSum += arr[i];
            }
            maxSum = max(maxSum, currSum);
        }
    }
    cout << "Maximum sum of subarray is: " << maxSum << endl;
}

int main() {
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr) / sizeof(int);
    maxSubArraySum(arr, n);
    return 0;
}
```

## Optimizing Subarray Sum Calculation

The above approach has a time complexity of O(n^3). You can optimize it to O(n^2) by avoiding the inner re-summation loop.

```cpp
#include <iostream>
#include <climits>
using namespace std;

void maxSubArraySum(int *arr, int n) {
    int maxSum = INT_MIN;
    for (int start = 0; start < n; start++) {
        int currSum = 0;
        for (int end = start; end < n; end++) {
            currSum += arr[end];
            maxSum = max(maxSum, currSum);
        }
    }
    cout << "Maximum sum of subarray is: " << maxSum << endl;
}

int main() {
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr) / sizeof(int);
    maxSubArraySum(arr, n);
    return 0;
}
```

## Kadane's Algorithm: Finding Maximum Subarray Sum in O(n)

Kadane's Algorithm is the most efficient way to find the maximum sum of a subarray in an array. It has a time complexity of O(n).

### Core Idea

The main idea behind Kadane's Algorithm is to maintain a running `currSum` and a `maxSum`. If `currSum` becomes negative, reset it to 0 because a negative sum will only decrease the sum of subsequent subarrays.

### Algorithm Steps

1.  Initialize `currSum = 0` and `maxSum = INT_MIN`.
2.  Iterate through the array.
3.  Add the current element to `currSum`.
4.  Update `maxSum` as `max(maxSum, currSum)`.
5.  If `currSum < 0`, reset `currSum = 0`.