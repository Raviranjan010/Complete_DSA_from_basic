#include <iostream>
#include <vector> // Include the vector header

using namespace std; // Required to use std names without prefix

int main() {
    vector<int> vec; // Declare a vector of integers

    cout << "Initial size of vector: " << vec.size() << endl;
    cout << "Initial capacity of vector: " << vec.capacity() << endl;

    vec.push_back(10);
    vec.push_back(20);

    cout << "Size of vector after adding elements: " << vec.size() << endl;
    cout << "Capacity of vector after adding elements: " << vec.capacity() << endl;

    vec.push_back(30);

    cout << "Size of vector after adding another element: " << vec.size() << endl;
    cout << "Capacity of vector after adding another element: " << vec.capacity() << endl;

    return 0; // Good practice to return from main
}
