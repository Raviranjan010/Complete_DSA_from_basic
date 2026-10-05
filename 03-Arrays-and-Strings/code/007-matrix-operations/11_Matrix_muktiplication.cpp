#include<iostream>
#include<vector>
using namespace std;

int main() {
    // Input dimensions for Matrix A
    int r1, c1;
    cout << "Enter rows and columns for Matrix A: ";
    cin >> r1 >> c1;

    vector<vector<int>> A(r1, vector<int>(c1));
    cout << "Enter elements of Matrix A:\n";
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            cin >> A[i][j];
        }
    }

    // Input dimensions for Matrix B
    int r2, c2;
    cout << "Enter rows and columns for Matrix B: ";
    cin >> r2 >> c2;

    // Initialize Matrix B
    vector<vector<int>> B(r2, vector<int>(c2));
    cout << "Enter elements of Matrix B:\n";
    for (int i = 0; i < r2; i++) {
        for (int j = 0; j < c2; j++) {
            cin >> B[i][j];
        }
    }

    // Check for matrix multiplication validity
    if (c1 != r2) {
        cout << "Matrix multiplication not possible. Columns of A must equal rows of B.\n";
        return 0;
    }

    // Initialize Result Matrix C
    vector<vector<int>> C(r1, vector<int>(c2, 0));

    // Matrix Multiplication
    cout << "Result of Matrix Multiplication:\n";
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            for (int k = 0; k < c1; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
            cout << C[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
