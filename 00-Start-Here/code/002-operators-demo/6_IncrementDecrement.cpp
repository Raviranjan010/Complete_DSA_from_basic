#include <iostream>
using namespace std;

int main() {
    int x = 10;
    double a = 11.4;

    int* intPtr = &x;
    double* doublePtr = &a;

    cout << "Value of x: " << x << endl;
    cout << "Address of x: " << &x << endl;

    cout << "Value of a: " << a << endl;
    cout << "Address of a: " << &a << endl;

    cout << "Value pointed to by intPtr: " << *intPtr << endl;
    cout << "Address stored in intPtr: " << intPtr << endl;
    cout << "Size of int variable: " << sizeof(x) << " bytes" << endl;
    cout << "Size of int pointer: " << sizeof(intPtr) << " bytes" << endl;
    cout << "Address of intPtr variable: " << &intPtr << endl;

    cout << "Address after intPtr + 1: " << (intPtr + 1) << endl;
    cout << "Address after intPtr + 2: " << (intPtr + 2) << endl;

    // Avoid dereferencing out-of-bounds pointers (undefined behavior)
    // cout << "Value at intPtr + 1: " << *(intPtr + 1) << endl;
    // cout << "Value at intPtr + 2: " << *(intPtr + 2) << endl;

    cout << "Value pointed to by doublePtr: " << *doublePtr << endl;
    cout << "Address stored in doublePtr: " << doublePtr << endl;
    cout << "Size of double pointer: " << sizeof(doublePtr) << " bytes" << endl;

    return 0;
}