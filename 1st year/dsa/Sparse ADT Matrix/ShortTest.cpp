#include <assert.h>
#include "header files/Matrix.h"
#include "header files/ShortTest.h"


using namespace std;

void testAll() { 
	Matrix m(4, 4);
	assert(m.nrLines() == 4);
	assert(m.nrColumns() == 4);	
	m.modify(1, 1, 5);
	assert(m.element(1, 1) == 5);
	TElem old = m.modify(1, 1, 6);
	assert(m.element(1, 2) == NULL_TELEM);
	assert(old == 5);
}

void testTranspose() {
    Matrix m(4, 4);
    m.modify(0,0,1);
    m.modify(0,1,2);
    m.modify(1,0,3);
    m.modify(1,1,4);
    m.transpose();
    assert(m.element(0,0)==1);
    assert(m.element(0,1)==3);
    assert(m.element(1,0)==2);
    assert(m.element(1,1)==4);
}
