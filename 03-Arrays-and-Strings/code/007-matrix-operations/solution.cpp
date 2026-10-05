#include <iostream>
#include <vector>
using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    vector<vector<int>> arr(m, vector<int>(n));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout<<"Enter rows and column ";
            cin >> arr[i][j];

        }
    }

    vector<vector<int>> transpose(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            transpose[i][j] = arr[j][i];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << "Transpose of matrix is: "<<transpose[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
