// example.cpp
#include <iostream>

extern "C" {
    void hello_from_cpp() {
        std::cout << "Hello from C++!" << std::endl;
    }

    int add_numbers(int a, int b) {
        return a + b;
    }
}
