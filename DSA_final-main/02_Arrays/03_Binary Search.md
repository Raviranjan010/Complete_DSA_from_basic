# Binary Search Algorithm 🔍

**Prerequisite**: The array must be sorted. Binary search is an efficient algorithm for finding a target value within a sorted array.

#include <iostream>
using namespace std;
// Binary Search function
int BinarySearch(int *arr, int n, int key) {
    int start = 0;
    int end = n - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == key) {
           return mid; // Key found at index mid
        }
        else if (arr[mid] < key) {
           start = mid + 1; // Search the right half
        }
        else {
           end = mid - 1; // Search the left half
        }
    }
    return -1;
}

int main() {
    // 🔑 ARRAY MUST BE SORTED
    int arr[] = {2, 3, 4, 5, 6, 33, 42};
    int n = sizeof(arr) / sizeof(int);
    cout << BinarySearch(arr, n, 4);
    return 0;
}



// ✔ Uses iterative binary search
// ✔ Uses overflow-safe mid calculation
// ✔ Correct termination condition
// ✔ Correct return values

// This is industry-standard binary search.
// 📝 Conceptual Explanation
// 🔧 Small Conceptual Cleanup (Comments)
// Your comment:


// // for even -> middle element =(first +end)/2
// // Last of first half
// Better and technically accurate version:

// Prerequisite: Array must be sorted
// mid = start + (end - start) / 2   (avoids overflow)
// If key < arr[mid] → search left half
// If key > arr[mid] → search right half

// ✅ Final Exam-Ready Version (Complete Program)
#include <iostream>
using namespace std;

int BinarySearch(int *arr, int n, int key) {
    int start = 0;
    int end = n - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == key)
           return mid; // Key found at index mid
        else if (arr[mid] < key)
           start = mid + 1; // Search the right half
        else
           end = mid - 1; // Search the left half
    }
    return -1; // key not found
}

int main() {
    int arr[] = {2, 5, 9, 13, 21, 30};
    int n = sizeof(arr) / sizeof(int);
    int key = 13;

   int result = BinarySearch(arr, n, key);
   if (result != -1)
       cout << "Element found at index: " << result << endl;
   else
        cout << "Element not found" << endl;

    return 0;
}
// 🧠 Binary Search Mental Model (Remember This)
// Always sorted array

// Divide → Compare → Discard half

// Loop continues until:

// Found → return index


// Range invalid → return -1

// ⏱ Time & Space Complexity (Must-Know)
// Metric	Value
// Time Complexity	O(log n)
// Space Complexity	O(1) (iterative)

// ❌ Returning wrong index or not returning -1

// time complexity of binary sort is log(n) -> 
// for 1st iteration n/2^0, for 2nd iteration n/n^1 ---> n/2^(x-1)
// by solving this x=log(base(2)n)=log(n)


// Override in array is not possible:
// int arr[5];
// cout<<arr<<'\n';
// int y=33;
// arr=&y;
// cout<<arr<<'\n';
// return 0;
// It will show error because pointers cannot be directly changed in an array 
// ❌ Why Error Occurs?
// arr is an array, not a pointer variable

// Array name represents a constant address

// You cannot change the base address of an array

// 👉 Array name = constant pointer

// ✅ Correct Explanation
// arr → base address of array

// &arr[0] → same as arr

// You cannot assign another address to arr

// ✅ Correct Example

// int arr[5] = {1,2,3,4,5};
// cout << arr << endl;      // address of first element
// cout << &arr[0] << endl; // same address

#include <iostream>
using namespace std;
int main(){
    int a=10;
    int *aptr=&a;
    cout<<aptr<<'\n';
    aptr++;
    cout<<aptr<<'\n';
    return 0;
}

// 📌 Explanation
// int takes 4 bytes

// aptr++ moves pointer by 4 bytes, not 1

// Addresses are in hexadecimal



// // integer exceed the memory by 4 bytes
// for example if address ending with 9 then next will be c due to increase in 4 bytes as here in hexadecimal format numbeing is like : 6789abcdefghijklmnop

// // ARITHEMATIC
// // adding constants
// if ptr+3 -> this statement means we adding  spaces of integer=12 spaces and /bytes 
// 3️⃣ Pointer Arithmetic Rules
// ✔ Allowed
// ptr + n

// ptr - n

// ptr2 - ptr1 (same array)

// ❌ Not Allowed
// ptr1 + ptr2

// ptr * ptr

// ptr / ptr

// 3️⃣ Pointer Arithmetic Rules
// ✔ Allowed
// ptr + n

// ptr - n

// ptr2 - ptr1 (same array)

// ❌ Not Allowed
// ptr1 + ptr2

// ptr * ptr

// ptr / ptr

int main(){
    int a=5;
    int *ptr=&a;
    cout<<ptr=&a;
    cout<<ptr<<"\n"; //first output
    ptr=ptr+3;
    cout<<(ptr-3)<<"\n"; //same value as previous output
    return 0;
}



void printArr(int *arr, int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    
}
int main(){
    int arr[]={2,4,55,323,21,32};
    int n=sizeof(arr)/sizeof(int);
    printArr(arr,n);
    return 0;
}
// elements printed
// 2 4 55 323 21 32
// 📌 Why It Works?
// arr → passed as pointer to first element

// arr[i] = *(arr + i)





//

// we can also write cout<<*(ptr+i)<<'\n'; for cout<<*ptr<<"\n";ptr=ptr+1;
// for
// add and subtract of pointers 
// addition of list address can not be happen because address cannot be added

int main(){
    int a=5;
    int *ptr=&a;
    int *ptr2=ptr1+3;
    cout<<ptr2<<"\n";
    cout<<ptr2-ptr1<<"\n";//it will give number of integer between them 
    return 0;
}
// if last digit of address is 64 then after subtraction  last digit will be 58 

// For array
int main(){
    int arr[20]={1,2,3,6,32,42,22};
    int ptr1=arr;
    int *ptr2=ptr1+3;
    cout<<*ptr2<<"\n"<<endl;
    cout<<*ptr1<<"\n"<<endl;
    cout<<ptr2-ptr1<<"\n"<<endl;
    return 0;


// Printing subarray 
#include<iostream>
using namespace std;
void printSubarray(int *arr,int n){
    for(int start=0;start<n;start++){
       for(int end=start;end<n;end++){
            cout<<"(" <<start<<","<<end<<")"<<"->"; //(0,0)->(0,1)->(0,2)....(1,1)->(1,2)....(n-1,n-1)
            for(int i=start;i<=end;i++){
                cout<<arr[i]<<" ";// for printing elements of subarray : (0,12,123,1234,12345   2,23,234,2345   3,34,345   6,32   32,42   42,22   22)
       }
            cout<<endl;
    }
}

// sum of elements of subarray
#include<iostream>
using namespace std;
void maxSubArraySum(int*arr,int n){
    int maxSum=INT_MIN;
    for(int start=0;start<n;start++){
       for(int end=start;end<n;end++){
            int Currsum=0;
            for(int i=start;i<=end;i++){
                Currsum+=arr[i];
            }
            maxSum=max(maxSum,Currsum);

    }
    cout<<"Maximum sum of subarray is: "<<maxSum<<endl;

}
int main(){
    int arr[]={2,4,55,323,21,32};
    int n=sizeof(arr)/sizeof(int);
    maxSubArraySum(arr,n);
    return 0;
}

// 🧠 Key Exam Summary (Memorize This)
// Arrays

// Array name = constant pointer

// Cannot reassign array

// Pointers
// Can change address

// Arithmetic depends on data type size

// Pointer Arithmetic
// ptr + n → jumps n elements

// ptr2 - ptr1 → number of elements

// Functions
// Array passed as pointer

// arr[i] == *(arr+i)
#include <iostream>
#include <climits>
using namespace std;

void maxSubArraySum(int *arr, int n) {
    int maxSum = INT_MIN;

    for (int start = 0; start < n; start++) {
        int currSum = 0;

        for (int end = start; end < n; end++) {
            currSum += arr[end];
            maxSum = max(maxSum, currSum);
        }
    }

    cout << "Maximum sum of subarray is: " << maxSum << endl;
}

int main() {
    int arr[] = {2, 4, 55, 323, 21, 32};
    int n = sizeof(arr) / sizeof(int);

    maxSubArraySum(arr, n);
    return 0;
}

// ⏱ Time Complexity
// O(n²)

// Improved from O(n³) by avoiding the inner re-summation loop.

// 🚀 BEST Approach: Kadane’s Algorithm (O(n))

// Either extend the current subarray

// Or start a new subarray at current element\




// ✅ Kadane’s Algorithm Code (Recommended)
#include <iostream>
#include <climits>
using namespace std;

void maxSubArraySum(int *arr, int n) {
    int currSum = 0;
    int maxSum = INT_MIN;

    for (int i = 0; i < n; i++) {
        currSum += arr[i];
        maxSum = max(maxSum, currSum);

        if (currSum < 0) {
            currSum = 0;
        }
    }

    cout << "Maximum sum of subarray is: " << maxSum << endl;
}

int main() {
    int arr[] = {2, 4, 55, 323, 21, 32};
    int n = sizeof(arr) / sizeof(int);

    maxSubArraySum(arr, n);
    return 0;
}

// ⏱ Time Complexity
// O(n)

// Best possible solution

// 🧠 Exam / Interview Memory Trick
// Approach	Time	Key Idea
// Brute Force	O(n³)	Check every subarray
// Optimized	O(n²)	Carry forward sum
// Kadane	O(n)	Drop negative sum
// Golden rule:

// If currentSum becomes negative → reset it

// ⚠️ Common Exam / Interview Traps
// ❌ Forgetting array must be sorted
// ❌ Using (start + end)/2 (overflow risk)
// ❌ Using start < end instead of start <= end
// ❌ Returning wrong index or not returning -1

// 📌 Key Points to Remember
// - Binary search requires a sorted array.
// - The middle element is calculated to divide the search space.
// - If the key is not found, the function returns -1.
// - Time complexity: O(log n), Space complexity: O(1).