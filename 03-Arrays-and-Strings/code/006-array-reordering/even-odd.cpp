// // difference of sum of elements at even and odd indices in a vector
// #include <iostream>
// #include <vector>
// using namespace std;
// int main(){
//     int arr[] = {1,2,3,5,3,2,22,24};
//     int sum_even = 0, sum_odd = 0; // Initialize sums for even and odd indices
//     for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) { // Loop through the array
//         if(i % 2 == 0) { // Check if the index is even
//             sum_even += arr[i]; // Add to even index sum
//         } else { // If the index is odd
//             sum_odd += arr[i]; // Add to odd index sum
//         }

//     }
//     int difference = sum_even - sum_odd; // Calculate the difference
//     cout << "Sum of elements at even indices: " << sum_even << endl; // Print sum of even indices
//     cout << "Sum of elements at odd indices: " << sum_odd << endl; // Print sum of odd indices
//     cout << "Difference (even - odd): " << difference << endl; // Print the difference
//     return 0; // Indicate successful execution
    
// }

#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int>v(5);
    cout<<"enter 5 elements";
    for(int i=0;i<5;i++){
        cin>>v[i];
    }
    
    int even_sum=0,odd_sum = 0;
    for(int i=0;i<5;i++){
        if(i%2==0){
            even_sum +=v[i];
        }

        else{
            odd_sum+=v[i];
        }

    }
    cout<<"Sum of elements at even indices are "<<even_sum<<endl;
    cout<<"Sum of elements at odd indices are "<<odd_sum<<endl;
    cout<<"difference of sum of odd and even indices is: "<<even_sum-odd_sum;

    return 0;
}