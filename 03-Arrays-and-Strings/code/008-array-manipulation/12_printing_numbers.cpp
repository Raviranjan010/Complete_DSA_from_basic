// Printing numbers from 1 to n using recursion factorial(int n) {
    // Base case: if n is 0 or 1, return 1


#include<iostream>
using namespace std;
// Function to print numbers from 1 to n using recursion
void printNumbers(int n) {
    if(n <=0 ) return; // Base case: if n is less than or equal to 0, stop recursion
    printNumbers(n - 1); // Recursive call with n-1
    cout<< n << " "; // Print the current number after the recursive call
}
int main() {
    int n = 10; // Example value for n
    cout << "Numbers from 1 to " << n << ": ";
    printNumbers(n); // Call the function to print numbers
    cout << endl; // Print newline after all numbers
    return 0; // Indicate successful execution


}
// This program demonstrates how to print numbers from 1 to n using recursion.
// The function `printNumbers` recursively calls itself with decremented values of n until it reaches
// the base case, where n is less than or equal to 0. After reaching the base case, it prints the numbers
// in ascending order as the recursive calls unwind.
// The output will be the numbers from 1 to n printed in ascending order.
