// Demonstration of pointer arithmetic and address increment in C++
#include <iostream>
using namespace std;

int main() {
    int arr[3] = {10, 20, 30};
    int* ptr = arr;

    cout << "Original address (ptr): " << ptr << ", value: " << *ptr << endl;

    // Increment pointer address (moves by sizeof(int) bytes)
    ptr++;
    cout << "After ptr++ address: " << ptr << ", value: " << *ptr << endl;

    ptr++;
    cout << "After next ptr++ address: " << ptr << ", value: " << *ptr << endl;

    return 0;
}
