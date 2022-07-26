#include "ListIterator.h"
#include "IndexedList.h"
#include <exception>

/// BC: theta(1)
/// WC: theta(1)
/// AC: theta(1)
ListIterator::ListIterator(const IndexedList& list) : list(list){
   this->current = this->list.head;
}

/// BC: theta(1)
/// WC: theta(1)
/// AC: theta(1)
void ListIterator::first(){
    this->current = this->list.head;
}

/// BC: theta(1)
/// WC: theta(1)
/// AC: O(1)
void ListIterator::next(){
    if(this->valid())
        this->current = this->list.array[this->current].next;
    else
        throw std::exception();
}

/// BC: theta(1)
/// WC: theta(1)
/// AC: theta(1)
bool ListIterator::valid() const{
    return this->current != -1;
}

/// BC: theta(1)
/// WC: theta(1)
/// AC: O(1)
TElem ListIterator::getCurrent() const{
    if(this->current != -1)
	    return this->list.array[this->current].info;
    else
        throw std::exception();
}