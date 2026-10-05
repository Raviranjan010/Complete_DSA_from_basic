// 
#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> v; // Declare a vector of integers
    v.insert(v.begin()+2, 10); // Insert 10 at index 2
    v.erase(v.begin()+2); // Erase the element at index 2
    v.push_back(20); // Add 20 to the end of the vector
    v.erase(v.end()-1); // Remove the last element (20)
    v.push_back(30); // Add 30 to the end of the vector
    v.insert(v.end(), 40); // Insert 40 at the end of the vector
    
}
