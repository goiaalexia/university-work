#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"

using namespace std;


// ADTList(interface with TPozition = Integer, IndexedList) –using a DLLA


int main(){
    testAll();
    testAllExtended();
    testRemoveLol();
    cout<<"Finished LI Tests!"<<endl;
}