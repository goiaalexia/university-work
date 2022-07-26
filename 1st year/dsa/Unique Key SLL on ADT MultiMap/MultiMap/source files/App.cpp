#include <iostream>
#include "header files/MultiMap.h"
#include "header files/ExtendedTest.h"
#include "header files/ShortTest.h"
#include "header files/MultiMapIterator.h"

using namespace std;


int main() {
// ADT MultiMap–using a SLL with unique keys.
// Every key will be associated with a SLL of the values belonging to that key.

    testAll();
    testAllExtended();
    cout << "End" << endl;

}
