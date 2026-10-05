// first and last occurence of a character in a string 
// 
#include<iostream>
using namespace std;
void findFirstAndLastOccurrence(string str, char ch, int *first , int *last){
    for(int i=0; i<str.length(); i++){
        if(str[i] == ch){
            *first =i;
            break; // Break after finding the first occurrence
        }
    }
    for(int i=str.length()-1; i>=0; i--){
        if(str[i] == ch){
            *last = i;
            break; // Break after finding the last occurrence
        }

    }
}

int main(){
    string str;
    char ch;
    cout << "Enter a string: ";
    getline(cin, str);
    cout << "Enter a character to find its first and last occurrence: ";
    cin >> ch;
    int first = -1 , last = -1;
    // Call the function to find first and last occurrence
    int *ptrFirst = &first;
    int *ptrLast = &last;
    // Using pointers to pass the addresses of first and last
    // Pass the addresses of 'first' and 'last' to update their values in the function
    findFirstAndLastOccurrence(str, ch, ptrFirst, ptrLast);
    // Display the results
    cout << "First occurrence of '" << ch << "' is at index: " << first << endl;
    cout << "Last occurrence of '" << ch << "' is at index: " << last << endl;
}