// Updating the value of a variable using a pointer
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    float y = 20.7;

    // Pointer to integer
    int* ptrX = &x;
    // Pointer to float
    float* ptrY = &y;

    cout << "Initial value of x is: " << *ptrX << endl;
    cout << "Initial value of y is: " << *ptrY << endl;

    // Updating the value using pointers
    *ptrX = 30;  // Update x through pointer
    *ptrY = 50.5; // Update y through pointer

    cout << "Updated value of x is: " << *ptrX << endl;
    cout << "Updated value of y is: " << *ptrY << endl;

    return 0;
}