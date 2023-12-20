# Example of creating a dynamic library in C++ using g++

This example demonstrates how to create a dynamic library in C++ using the GNU C++ compiler (g++) and use it in Python using ctypes.

## Steps

1. **Install MinGW:**
    - Download the MinGW installer from [MinGW official website](https://mingw-w64.org/doku.php).
    - Run the installer and select components that include `g++`.
    - Add `C:\mingw-w64\mingw64\bin` (or the path corresponding to your installation) to the PATH environment variable.

2. **Compiling C++ code:**
    - Create a file `example.cpp` with your C++ code.
    - Open a command prompt and run the following command to compile the code and create the dynamic library:

      ```bash
      g++ -shared -o example.dll -fPIC example.cpp
      ```

      (On Windows the library extension will be `.dll`)

3. **Running Python code:**
    - Create a file `example.py` with code that uses the dynamic library.
    - Run the `example.py` file:

      ```bash
      python example.py
      ```

4. **Result:**
    - You should see the output of the message from the C++ code and the result of executing the functions in Python.

## Important notes:

- Check that the PATH variable contains the path to the directory with the g++ executable file.
- Make sure your code compiles without errors before using the library in Python.
- If used on other platforms, please note the differences in library extensions (.so on Linux, .dylib on macOS).
