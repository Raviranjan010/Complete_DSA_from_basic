// #include <iostream>
// using namespace std;

// // Recursive function to remove all occurrences of 'a' from a string
// string removeA(const string &s, int idx) {
//     // Base case: if index reaches the end of the string, return empty string
//     if (idx == s.length()) return "";

//     // If current character is 'a', skip it and recurse for the rest
//     if (s[idx] == 'a') {
//         return removeA(s, idx + 1);
//     } else {
//         // Otherwise, include current character and recurse
//         return s[idx] + removeA(s, idx + 1);
//     }
// }

// int main() {
//     string s = "adeedeqwiaawsettfd";
//     cout << removeA(s, 0);
//     return 0;
// }


#include<iostream>
using namespace std;
// Function to remove all occurrences of 'a' from a string using recursion
string f(const string &s, int idx, int n) {
    if(idx == n) return ""; // Base case: if index reaches the end of the string, return empty string
    if(s[idx] == 'a') {
        return f(s, idx+1, n); // Skip 'a'
    } else {
        return string(1, s[idx]) + f(s, idx+1, n); // Include current character
    }
}
int main() {
    string s = "adeedeqwiaawsettfd";
    int n = s.length();
    cout << f(s, 0, n);
    return 0;
}