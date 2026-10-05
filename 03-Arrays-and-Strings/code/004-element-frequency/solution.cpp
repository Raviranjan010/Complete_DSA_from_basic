// frequency of query elements in a vector
#include <iostream>
#include<vector>
using namespace std;
int main() {
    vector<int> v(10); 
    cout << "Enter 10 elements: ";
    for(int i = 0; i <10; i++) {
        cin >> v[i]; // Take input for the vector

    }
    // cout << "Enter the number of queries: ";
    const int N = 1e5 +10; // Maximum size for the frequency array
    vector<int> freq(N, 0); // Initialize frequency array with zeros
    for(int i = 0; i < 10; i++) {
        freq[v[i]]++; // Increment the frequency of each element in the vector
    }
    cout << "Enter the number of queries: ";
    int q;
    cin >> q; // Take input for the number of queries
    cout << "Enter the queries: ";
    while(q--) {
        int x;
        cin >> x; // Take input for each query
        cout << freq[x] << " "; // Output the frequency of the queried element
    }
    cout << endl; // Print a newline after all queries
    return 0; // Indicate successful execution
    

}
// difference between enter query and enter the number of queries:
// "Enter the number of queries" is asking how many queries you will input.
// "Enter the queries" is asking for the actual values of those queries.

/*// frequency of query elements in a vector
#include <iostream>   // For standard input/output
#include <vector>     // For using vectors
using namespace std;  // To avoid writing std:: before every I/O or vector
cpp
Copy code
int main() {
The main function: Entry point of your C++ program.

cpp
Copy code
    vector<int> v(10); 
Creates a vector v of size 10, initialized with zeros by default.

cpp
Copy code
    cout << "Enter 10 elements: ";
Prompts the user to enter 10 integers.

cpp
Copy code
    for(int i = 0; i < 10; i++) {
        cin >> v[i]; // Take input for the vector
    }
A loop to input 10 elements from the user into the vector v.

cpp
Copy code
    const int N = 1e5 + 10;
Declares a constant N which equals 100010.

This is used as the maximum size for the frequency array to handle values from 0 up to 100000.

cpp
Copy code
    vector<int> freq(N, 0);
Creates a vector freq of size N, initializing all elements to 0.

freq[x] will store the number of times x appears in the input vector v.

cpp
Copy code
    for(int i = 0; i < 10; i++) {
        freq[v[i]]++; // Increment the frequency of each element in the vector
    }
For each element in v, increment its corresponding count in freq.

cpp
Copy code
    cout << "Enter the number of queries: ";
Asks how many queries the user will perform (how many elements' frequencies they want to know).

cpp
Copy code
    int q;
    cin >> q; // Take input for the number of queries
Reads the number of queries.

cpp
Copy code
    cout << "Enter the queries: ";
Prompts user to enter each query value one by one.

cpp
Copy code
    while(q--) {
        int x;
        cin >> x; // Take input for each query
        cout << freq[x] << " "; // Output the frequency of the queried element
    }
While there are queries left:

Read the queried value x.

Print how many times x appeared in the original vector using freq[x].

cpp
Copy code
    cout << endl; // Print a newline after all queries
    return 0; // Indicate successful execution
}
Ends the output with a newline for neatness.

Returns 0 to indicate the program ended successfully.

🔍 Clarification:
"Enter the number of queries"
→ Asking how many values you will check the frequency for.

"Enter the queries"
→ Asking you to input the actual values (like 5, 8, etc.) to check their frequency.

*/