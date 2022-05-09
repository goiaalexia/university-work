#include <iostream>
#include "header files/Matrix.h"
#include "header files/ExtendedTest.h"
#include "header files/ShortTest.h"
using namespace std;


int main() {
    testAll();
    testAllExtended();
    testTranspose();
	cout << "Test End" << endl;
    return 0;
}