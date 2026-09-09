// manipulation of arrays in C++ Find the unique number in a given Array where all the elements are being repeated twice with one value being unique.
// it is a common problem in competitive programming and interviews. The solution can be efficiently implemented using the XOR operation, which has the property that `a ^ a = 0` for any integer `a`, and `a ^ 0 = a`. This means that if we XOR all the numbers in the array, the pairs will cancel each other out, leaving only the unique number.
#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector<int> arr = {1,2,7,7,3,6,2};
    for(int i = 0; i<arr.size(); i++){
        for(int j = i + 1; j < arr.size(); j++){
            if(arr[i]== arr[j]){
                // If a duplicate is found, remove it from the vector
                arr[i] = arr[j] = -1; // Mark duplicates as -1

            }

        }
    }
    // Print the unique elements
    int uniqueCount = 0; // Counter for unique elements
    for(int i = 0; i<arr.size(); i++){
        if(arr[i] != -1){ // Check if the element is not marked as -1
            cout << arr[i] << " "; // Print the unique element
            uniqueCount++;
             // Increment the unique count
        }

    }
    if(uniqueCount == 0) {
        cout << "No unique elements found." << endl; // If no unique elements are found
    } else {
        cout << endl; // Print a newline for better readability
    }
}
// This code iterates through the vector, marks duplicates as -1, and then prints the unique elements.
// It also counts the number of unique elements and prints a message if none are found.
// This approach has a time complexity of O(n^2) due to the nested loops, which is not optimal for large arrays.
// A more efficient solution would be to use a hash map or set to track duplicates, or to use the XOR operation as mentioned earlier.
