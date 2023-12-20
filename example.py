# example.py
import ctypes

# Load the C++ library
cpp_lib = ctypes.CDLL('./example.so')

# Call a function from C++
cpp_lib.hello_from_cpp()

# Call a function with parameters
result = cpp_lib.add_numbers(3, 4)
print(f"Addition result: {result}")
