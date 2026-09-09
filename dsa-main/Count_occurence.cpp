// Occurrence of elements in a vector
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v(10); // Pre-size the vector to hold 10 elements

    cout << "Enter 10 elements: ";
    for(int i = 0; i < 10; i++) {
        cin >> v[i]; // Take input
    }

    cout << "Enter the element to find its occurrence: ";
    int element;
    cin >> element;

    int count = 0;
    for(int i = 0; i < v.size(); i++) {
        if(v[i] == element) {
            count++;
        }
    }

    if(count == 0) {
        cout << "Element not found in the vector." << endl;
    } else {
        cout << "The element " << element << " occurs " << count << " times in the vector." << endl;
    }

    return 0;
}
