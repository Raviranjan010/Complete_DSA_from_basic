// Adding and removing elements from a vector in C++ can be done using various methods.
// // Here is a simple example demonstrating how to add and remove elements from a vector:
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> vec; // Declare a vector of integers

    // Adding elements to the vector
    vec.push_back(10); // Add 10 to the end of the vector
    vec.push_back(20); // Add 20 to the end of the vector
    vec.push_back(30); // Add 30 to the end of the vector

    cout << "Vector after adding elements: ";
    for (int element : vec) {
        cout << element << " "; // Print each element in the vector
    }
    cout << endl;


    // Removing an element from the vector
    vec.pop_back(); // Remove the last element (30)

    cout << "Vector after removing last element: ";
    for (int element : vec) {
        cout << element << " "; // Print each element in the vector
    }
    cout << endl;
    // Inserting an element at a specific position
    vec.insert(vec.begin() + 1, 15); // Insert 15 at index 1
    cout << "Vector after inserting 15 at index 1: ";
    for (int element : vec) {
        cout << element << " "; // Print each element in the vector
    }
    cout << endl;

    // Erasing an element at a specific position
    vec.erase(vec.begin() + 1); // Erase the element at index 1 (15)
    cout << "Vector after erasing element at index 1: ";
    for (int element : vec) {
        cout << element << " "; // Print each element in the vector
    }
    cout << endl;

    return 0; // Indicate successful execution
}

