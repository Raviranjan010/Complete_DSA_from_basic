#include <iostream>
#include <vector>

std::vector<int> computeSPF(int n) {
    std::vector<int> spf(n + 1);
    for (int i = 0; i <= n; ++i) spf[i] = i;

    for (int p = 2; p * p <= n; ++p) {
        if (spf[p] == p) {
            for (int i = p * p; i <= n; i += p) {
                if (spf[i] == i) spf[i] = p;
            }
        }
    }
    return spf;
}

std::vector<int> factorize(int x, const std::vector<int>& spf) {
    std::vector<int> factors;
    while (x > 1) {
        factors.push_back(spf[x]);
        x /= spf[x];
    }
    return factors;
}

int main() {
    int maxLimit = 100;
    auto spf = computeSPF(maxLimit);
    int num = 84;
    auto factors = factorize(num, spf);
    std::cout << "Prime factors of " << num << ": ";
    for (int f : factors) std::cout << f << " ";
    std::cout << "\n";
    return 0;
}
