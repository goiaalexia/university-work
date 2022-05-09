#include <assert.h>
#include <exception>
#include <iostream>
#include <vector>
#include <algorithm>
#include "ExtendedTest.h"
#include "IndexedList.h"
#include "ListIterator.h"

using namespace std;

void testIteratorSteps(IndexedList& l) {
	int count = 0;
	ListIterator it = l.iterator();
	while (it.valid()) {
		count++;
		it.next();
	}
	assert(count == l.size());
}

void testCreate() {
	cout << "Test create" << endl;
    IndexedList list = IndexedList();
    assert(list.isEmpty());
    ListIterator it = list.iterator();
    assert(!it.valid());
    try {
        it.next();
        assert(false);
    } catch (exception &) {
        assert(true);
    }
    assert(list.size() == 0);
}

void testAdd() {
	cout << "Test add" << endl;
    IndexedList list = IndexedList();
    list.addToEnd(1);
    assert(!list.isEmpty());
    assert(list.size() == 1);
    assert(list.getElement(0) == 1);
    try {
        list.getElement(2);
        assert(false);
    } catch (exception&){
        assert(true);
    }
	testIteratorSteps(list);
    for (int i = 0; i <= 100; i ++){
        list.addToEnd(i);
        list.addToPosition(list.size() - 1,i);
        try {
            list.addToPosition((i+2)*2,i);
            assert(false);
        } catch (exception&){
            assert(true);
        }
		testIteratorSteps(list);
        assert(list.size() == 2*(i+1) + 1);
    }
    ListIterator it = list.iterator();
    assert(it.getCurrent() == 1);
    it.next();
    int i = 0;
    while (it.valid()){
        assert(it.getCurrent() == i);
        it.next();
        assert(it.getCurrent() == i);
        it.next();
        i++;
    }
    assert(!it.valid());
    try {
        it.getCurrent();
        assert(false);
    } catch (exception&){
        assert(true);
    }
    it.first();
    assert(it.valid());
    assert(it.getCurrent() == 1);

    i = 1;
    int v = 0;
    while (i < list.size()){
        assert(list.getElement(i) == v);
        i++;
        i++;
        v++;
    }
}

void testSetRemoveSearch() {
	cout << "Test set, remove and search " << endl;
    IndexedList list = IndexedList();
    for (int i = 0; i <= 100; i ++){
        list.addToEnd(i);
    }
    assert(list.size() == 101);
	testIteratorSteps(list);
    assert(list.search(50) == 50);
    assert(list.search(100) == 100);
    assert(list.remove(100) == 100);
    try {
        list.remove(100);
        assert(false);
    } catch (exception&){
        assert(true);
    }
    assert(list.size() == 100);
    assert(list.search(100) == -1);
    assert(list.search(99) == 99);
    int v = 99;
    for (int i = 0; i < 100; i++){
        list.setElement(i,v);
        v--;
    }
    assert(list.getElement(99) == 0);
    assert(list.search(99) == 0);
    assert(list.search(0) == 99);
    assert(list.search(50) == 49);
	testIteratorSteps(list);
    try {
        list.setElement(v,v);
        assert(false);
    } catch (exception&){
        assert(true);
    }
    ListIterator it = list.iterator();
    for (int i = 99; i > -1; i--){
        assert(it.getCurrent() == i);
        it.next();
    }
    assert(!it.valid());
    for (int i = 99; i > -1; i--){
        list.remove(i);
        assert(list.size() == i);
    }
    assert(list.isEmpty());
    assert(list.size() == 0);
    it.first();
    assert(!it.valid());
}

void testQuantity() {
	cout << "Test quantity" << endl;
	IndexedList l1;
	int pos = 3;
	for (int i = -10000; i <= 5000; i++) {
		if (l1.size() < 6) {
			l1.addToEnd(i);
		}
		else {
			l1.addToPosition(pos, i);
			pos = (pos + 11) % l1.size();
		}
	}

	testIteratorSteps(l1);
	assert(l1.size() == 15001);
	for (int i = 0; i < l1.size() ; i = i + 3) {
		l1.remove(i);
	}
	testIteratorSteps(l1);
	for (int i = 0; i < 20000; i = i + 5) {
		l1.addToEnd(i);
	}
	testIteratorSteps(l1);

	IndexedList l2;
	pos = 1;
	for (int i = -100000; i <= 100000; i = i + 7) {
		if (l2.size() < 5) {
			l2.addToEnd(i);
		}
		else {
			l2.addToPosition(pos, i);
			pos = (pos + 7) % l2.size();
		}
	}
	ListIterator listIt = l2.iterator();
	pos = 0;
	while (listIt.valid()) {
		TElem te = listIt.getCurrent();
		assert(l2.search(te) == pos);
		pos++;
		listIt.next();
	}
	for (int i = 0; i < l2.size(); i++) {
		TElem elem = l2.getElement(i);
		assert(l2.search(elem) == i);	
	}
	testIteratorSteps(l2);
	for (int i = -30000; i < 300000; i++) {
		int pos = l2.search(i);
		if (pos != -1) {
			assert(l2.remove(pos) == i);
		}		
	}
	testIteratorSteps(l2);
}

void compareListMinusPosition(IndexedList& l1, IndexedList& l2, int pos) {
	assert(l1.size() == l2.size() + 1);
	for (int i = 0; i < l2.size(); i++) {
		if (i < pos) {
			assert(l1.getElement(i) == l2.getElement(i));
		}
		else if (i > pos) {
			assert(l1.getElement(i + 1) == l2.getElement(i));
		}
	}
}

void testRemove() {
	cout << "Test remove" << endl;
	IndexedList list1;
	IndexedList list2;
	for (int i = 0; i < 100; i++) {
		list1.addToEnd(i);
		list1.addToPosition(0, 2 * i);
		list2.addToEnd(i);
		list2.addToPosition(0, 2 * i);
	}
	for (int i = 0; i < list1.size(); i++) {
		assert(list1.getElement(i) == list2.getElement(i));
	}

	int pos = 4;
	testIteratorSteps(list1);
	for (int i = 0; i < 50; i++) {
		list2.remove(pos);
		compareListMinusPosition(list1, list2, pos);
		list1.remove(pos);
		pos = (pos + 7) % list2.size();
	}
	testIteratorSteps(list2);

}

void testAllExtended() {
    testCreate();
    testAdd();
    testSetRemoveSearch();
	testRemove();
	testQuantity();
}
