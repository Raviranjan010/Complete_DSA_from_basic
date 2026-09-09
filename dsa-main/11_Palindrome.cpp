#include<iostream>  // Include the input-output stream library
using namespace std; // Use the standard namespace to avoid writing std:: repeatedly

// Recursive function to check if a number is a palindrome
bool isPalindrome(int num, int* temp) {
    // Base case: If the number has only one digit (0 to 9)
    if (num >= 0 && num <= 9) {
        int lastDigit = *temp % 10;  // Get the last digit of the number using the pointer
        *temp /= 10;                 // Remove the last digit from temp
        return (num == lastDigit);  // Compare the current digit from left and right
    }

    // Recursive case: Process the number from left to right
    // Step 1: Recur for the number without its last digit
    // Step 2: After recursion, compare the current digit from the left (`num % 10`)
    //         with the current digit from the right (`*temp % 10`)
    bool result = isPalindrome(num / 10, temp) && (num % 10 == *temp % 10);

    *temp /= 10; // Remove the last digit from temp for the next comparison
    return result; // Return the result of current comparison
}

int main() {
    int num = 21212;    // The original number to check
    int copy = num;     // Create a copy of the number (used to compare digits from the end)
    int* temp = &copy;  // Pointer to the copy, used to manipulate and track digits from the right

    // Call the recursive function and print the result
    cout << "Is " << num << " a palindrome? "
         << (isPalindrome(num, temp) ? "Yes" : "No") << endl;

    return 0; // Indicate successful execution
}
