// Printing the value of address using pointer
#include <iostream>
using namespace std;
int main(){
    int x = 10;
    float y = 20.7;

    // Pointer to integer
    int* ptrX = &x;
    // Pointer to float
    float* ptrY = &y;

    cout << "Value of x is: " << *ptrX << endl;
    cout << "Value of y is: " << *ptrY << endl;
    
    cout << "Address of x is: " << ptrX << endl;
    cout << "Address of y is: " << ptrY << endl;

    return 0;
}