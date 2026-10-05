// sum of 3 numbers: This function takes three integers as input and returns their sum.
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> arr = {1,2,3,4,5,3}; // Initialize a vector with some integers
    int target_sum = 6; // Define the target sum we want to find triplets for
    bool found = false; // Flag to indicate if any triplet is found
    // Iterate through the vector to find triplets that sum up to target_sum
    for (int i = 0; i<arr.size();i++){
        for(int j = i +1 ; j < arr.size(); j++){
            for(int k = j +1 ; k < arr.size() ; k++){
                if(arr[i] + arr[j] + arr[k] == target_sum) {
                    cout << "Triplet found: (" << arr[i] << ", " << arr[j] << ", " << arr[k] << ")" << endl;
                    found = true; // Set flag to true if a triplet is found
                }

            }

            
        }

    }
    if (!found) {
        cout << "No triplets found that sum up to " << target_sum << endl; // If no triplets are found
    }
    return 0; // Indicate successful execution

}