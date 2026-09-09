#include<iostream>
using namespace std;
int main(){
    int x = 10;
    float y=20.7;
    cout<< "Value of x is: " << x << endl;
    cout << "Value of y is: " << y << endl;
    cout << "Size of x is: " << sizeof(x) << " bytes" << endl;
    cout << "Size of y is: " << sizeof(y) << " bytes" <<
    endl;
    cout<<"Address of x is: " << &x << endl;
    cout<<"Address of y is: " << &y << endl;
    return 0;
}