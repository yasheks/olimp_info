#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int A, B, C, D;
    cin >> A >> B >> C >> D;

    int a[] = {A, B, C};
    int gg = *max_element(a, a + 3);
    int ggg = A + B + C - gg;
    int h = ggg - gg;

    if (h < 0) {
        h = -h;
    }

    int t = h - D;
    if (t < 0) {
        t = 0;
    }

    cout << t << endl;
    return 0;
}
