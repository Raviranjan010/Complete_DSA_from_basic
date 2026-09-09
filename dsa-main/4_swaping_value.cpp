// Swapping values using pointers in C++
#include <iostream>
using namespace std;
void swap(int* a, int* b) {
    int temp = *a; // Store the value pointed to by a in temp
    *a = *b;       // Update the value pointed to by a with the value pointed to by b
    *b = temp;    // Update the value pointed to by b with the value stored in temp
}
int main() {
    int x = 5;
    int y = 10;
    int* ptrX = &x; // Pointer to x
    int* ptrY = &y; // Pointer to y 
    // Display initial values
    cout << "Initial value of x is: " << *ptrX << endl;
    cout << "Initial value of y is: " << *ptrY << endl;
    // Swapping values using pointers
    swap(ptrX, ptrY);
    // Display swapped values
    cout << "Swapped value of x is: " << *ptrX << endl;
    cout << "Swapped value of y is: " << *ptrY << endl;
    // Example of swapping two integers using pointers
    

    cout << "Before swapping: x = " << x << ", y = " << y << endl;

    // Call swap function with addresses of x and y
    swap(&x, &y);

    cout << "After swapping: x = " << x << ", y = " << y << endl;

    return 0;
}


