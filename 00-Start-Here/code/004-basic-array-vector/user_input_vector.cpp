// Taking user input to fill a vector
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;

    // Taking 5 inputs from the user
    for (int i = 0; i < 5; i++) {
        int element;
        cin >> element;          // Take input from the user
        v.push_back(element);    // Add the element to the vector
    }

    // Printing using index-based for loop
    for (int i = 0; i < 5; i++) {
        cout << v[i] << " ";     // Print each element
        // cout<< "By for loop";  
    }
    cout << endl;

    // Printing using range-based for loop
    for (int element : v) {
        cout << element << " ";
    }
    cout << endl;

    // Printing using while loop
    int i = 0;
    while (i < v.size()) {
        cout << v[i] << " ";
        i++;
    }
    cout << endl;

    return 0; // Indicate successful execution
}
