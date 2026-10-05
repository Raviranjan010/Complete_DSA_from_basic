// checking if prefix sum of a part is equal to other part
// this is a common problem to check if the prefix sum of a part of an array is equal to the other part
// this can be done using prefix sum
#include<iostream>
#include<vector>
using namespace std;
bool check_prefix_sum(vector<int> &v){
    int total_sum = 0;
    for(int i = 0; i<v.size(); i++){
        total_sum += v[i]; // Calculate the total sum of the array  
    }
    int prefix_sum = 0;
    for(int i = 0; i<v.size()-1; i++){
        prefix_sum += v[i]; // Calculate the prefix sum up to the current index 
        int suffix_sum = total_sum - prefix_sum;
        if(prefix_sum == suffix_sum) {
            return true; // If prefix sum equals suffix sum, return true
        }


    }
    return false; // If no such prefix sum found, return false

}
int main( ) {
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    vector<int> v; // Declare a vector to hold the elements)
    cout << "Enter the elements of the array: ";
    for(int i = 0; i<n; i++ ){
        int elemnts;
        cin >> elemnts; // Take input for each element
        v.push_back(elemnts); // Add the element to the vector


    }
    if(check_prefix_sum(v)) {
        cout << "There exists a prefix sum that equals the suffix sum." << endl; // If such a prefix sum exists
    } else {
        cout << "No prefix sum equals the suffix sum." << endl; // If no such prefix sum exists
    }
    return 0; // Indicate successful execution
}