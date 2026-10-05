#include <iostream>
using namespace std;

int main() {
    int arr[7] = {7, 2, 4, 6, 8, 4};
    int* ptr = arr; // Pointer to the first element

    cout << "Value before increment: " << *ptr << endl;
    (*ptr)++; // Increment the value pointed to by ptr
    
    cout << "Value after increment: " << *ptr << endl;
    cout << "First element of array: " << arr[0] << endl;

    return 0;
}