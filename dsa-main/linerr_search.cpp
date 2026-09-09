// Linear search algorithm implementation in C++14
// #include <iostream>
// int main(){
//     int arr1[] = {10, 20, 30, 40, 50};

//     int n = sizeof(arr1) / sizeof(arr1[0]); // Calculate the number of elements in the array
//     int key = 30; // Element to search for
//     bool found = false; // Flag to indicate if the element is found
//     for (int i = 0; i < n; i++) {
//         if (arr1[i] == key) {
//             found = true; // Element found
//             std::cout << "Element " << key << " found at index " << i << std::endl;
//             break; // Exit the loop once the element is found
//         }
        
//     }

// }
#include <iostream>
using namespace std;

int main() {
    int a[] = {1, 3, 56, 13, 32, 7};
    int key = 7;
    int ans = -1;
    int size = sizeof(a) / sizeof(a[0]);  // Calculate total size of array

    for (int i = 0; i < size; i++) {
        if (a[i] == key) {
            ans = i;
        }
    }

    cout << ans << endl;
    return 0;
}
