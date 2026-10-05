// if unique elementt present in the array 


#include <iostream>
#include <vector>
#include <climits>  // ✅ Needed for INT_MIN

using namespace std;

int LargestElement(int arr[], int size) {
    int max = INT_MIN;
    int maxindex = -1;
    for (int i = 0; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
            maxindex = i;
        }
    }
    return maxindex;
}

int main() {
    int array[] = {10, 30, 70, 20, 44, 32, 43, 50};  // ✅ Correct array declaration
    int index = LargestElement(array, 8);
    cout << "The largest element is at index: " << index << ", value: " << array[index] << endl;
    return 0;
}
