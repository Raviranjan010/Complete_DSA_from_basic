// sum of previous numbers in prefix sum
// it is a common problem to find the sum of all previous numbers in an array
// this can be done using prefix sum
#include <iostream>
#include<vector>
using namespace std;
void running_sum(vector<int> &v){
    for(int i =1; i< v.size(); i++){
        v[i] += v[i-1]; // Add the previous element to the current element

    }
    cout << "Running sum of the array: ";
    for(int i =0; i< v.size(); i++){
        cout << v[i] << " "; // Print the running sum
    }
    cout << endl; // Print a newline for better readability
}
int main() {
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    vector<int> v; // Declare a vector to hold the elements
    cout << "Enter the elements of the array: ";
    for(int i = 0; i<n ; i++) {
        int element;
        cin >> element; // Take input for each element
        v.push_back(element); // Add the element to the vector

    }
    running_sum(v);
    return 0; // Indicate successful execution
    
}