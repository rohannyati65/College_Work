#include <iostream>
using namespace std;

void add(int a, int b) {
    cout << a + b;
}

void subtract(int a, int b) {
    cout << a - b;
}

void multiply(int a, int b) {
    cout << a * b;
}
void(*fun_ptr_arr[])(int, int) = ____________________;    // LINE-1


void caller(int ch, int a, int b) {

    if (ch > 2) return;

    ____________________;    // LINE-2
}
int main() {

    int ch, a, b;

    cin >> ch >> a >> b;

    caller(ch, a, b);

    return 0;
}
