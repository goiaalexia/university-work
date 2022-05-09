#include <assert.h>
#include <exception>
#include <iostream>
#include "ShortTest.h"
#include "IndexedList.h"
#include "ListIterator.h"




void testAll() {
    IndexedList list = IndexedList();
    assert(list.isEmpty());
    list.addToEnd(1);
    assert(list.size() == 1);
    list.addToPosition(0,2);
    assert(list.size() == 2);
    ListIterator it = list.iterator();
    assert(it.valid());
    it.next();
    assert(it.getCurrent() == 1);
    it.first();
    assert(it.getCurrent() == 2);
    assert(list.search(1) == 1);
    assert(list.setElement(1,3) == 1);
    assert(list.getElement(1) == 3);
    assert(list.remove(0) == 2);
    assert(list.size() == 1);
}

void testRemoveLol() {
    IndexedList list = IndexedList();
    for (int i = 0; i <= 100; i++) {
        list.addToEnd(i);
    }
    for (int i = 0; i < list.size(); i++) {
        std::cout << list.getElement(i) << " ";
    }
    std::cout << std::endl;
    list.removeBetween(0, 3);
    for (int i = 0; i < list.size(); i++) {
        std::cout << list.getElement(i) << " ";
    }
    list.removeBetween(1, 1);
    std::cout << std::endl;
    for (int i = 0; i < list.size(); i++) {
        std::cout << list.getElement(i) << " ";
    }
    try {
        list.removeBetween(-1, -302);
        assert(false);
    } catch (std::exception &) {
        assert(true);
    }
    std::cout<<std::endl;
}