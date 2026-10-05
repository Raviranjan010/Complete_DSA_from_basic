#include <iostream>
using namespace std;

// --- Function Declarations (Prototypes) ---
void sayHello();
int Sum(int a, int b);
int SumDefault(int a = 3, int b = 7); // Default arguments
bool isEven(int n);
int Fact(int n);
bool isPrime(int n);

// --- Main Function ---
int main() {
    // 1. Simple Function Call
    sayHello();

    // 2. Function with Parameters and Return
    int n = 12, m = 10;
    cout << "Sum of " << n << " and " << m << " is: " << Sum(n, m) << endl;

    // 3. Default Arguments
    cout << "SumDefault(10): " << SumDefault(10) << endl; // a=10, b=7 (default)
    cout << "SumDefault(): " << SumDefault() << endl;     // a=3 (default), b=7 (default)

    // 4. Even or Odd
    int num = 6;
    if (isEven(num)) {
        cout << num << " is Even" << endl;
    } else {
        cout << num << " is Odd" << endl;
    }

    // 5. Factorial
    int f = 5;
    cout << "Factorial of " << f << " is: " << Fact(f) << endl;

    // 6. Prime Check
    int p = 17;
    if (isPrime(p)) {
        cout << p << " is Prime" << endl;
    } else {
        cout << p << " is not Prime" << endl;
    }

    return 0;
}

// --- Function Definitions ---

void sayHello() {
    cout << "Hello World\n";
}

int Sum(int a, int b) {
    return a + b;
}

int SumDefault(int a, int b) {
    return a + b;
}

bool isEven(int n) {
    if (n % 2 == 0)
        return true;
    else
        return false;
}

int Fact(int n) {
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

// Optimized Prime Check
bool isPrime(int n) {
    if (n <= 1) return false;

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}
