#include <exception>

#include "IndexedList.h"
#include "ListIterator.h"

#include <iostream>

/// BC: theta(capacity)
/// WC: theta(capacity)
/// AC: O(capacity)
IndexedList::IndexedList() {
    this->capacity = 2;
    this->array = new DLLANode[this->capacity];
    for (int i = 0; i < this->capacity; i++) {
        this->array[i].next = NULL_TELEM;
        this->array[i].prev = NULL_TELEM;
        this->array[i].info = NULL_TELEM;
    }
    this->head = -1;
    this->tail = -1;
    this->first_free = -1;
    this->length = 0;

}

/// BC: theta(1)
/// WC: theta(1)
/// AC: O(1)
int IndexedList::size() const {
    return this->length;
}

/// BC: theta(1)
/// WC: theta(1)
/// AC: O(1)
bool IndexedList::isEmpty() const {
    if (this->length == 0)
        return true;
    return false;
}

/// BC: theta(1) (throws exception or first element)
/// WC: theta(length) (last element)
/// AC: O(length)
TElem IndexedList::getElement(int pos) const {
    int current = this->head;
    int counter = 0;
    if (pos > this->length)
        throw std::exception();
    while (current != -1) { // while we haven't reached the end
        if (counter == pos)
            return this->array[current].info; // if we found the element, we return it
        else {
            current = this->array[current].next;
            counter++;
        }
    }
    throw std::exception();
}

/// BC: theta(1) (throws exception or first element)
/// WC: theta(length) (last element)
/// AC: O(length)
TElem IndexedList::setElement(int pos, TElem e) {
    int counter = 0;
    int current = this->head;
    if (pos > this->length)
        throw std::exception();
    while (current != -1) {
        if (counter == pos) {
            TElem copy = this->array[current].info;
            this->array[current].info = e;
            return copy;
        } else {
            current = this->array[current].next;
            counter++;
        }
    }
    throw std::exception();
}

/// BC: theta(1)
/// WC: theta(capacity+length) (resize and last free)
/// AC: O(capacity) (usually we don't have to resize)
void IndexedList::addToEnd(TElem e) {
    if (this->first_free == -1) { // we search for the first free space in the array

        if (this->length >= this->capacity) { // if there are none, we resize the array
            this->capacity *= 2;
            auto *new_arr = new DLLANode[this->capacity];
            for (int i = 0; i < this->length; i++) {
                new_arr[i] = this->array[i];
            }
            for (int i = this->length; i < this->capacity; i++) {
                new_arr[i].next = new_arr[i].prev = new_arr[i].info = NULL_TELEM;
            }
            delete[] this->array;
            this->array = new_arr;
        }

        this->initFreeSpace();
    }

    int copy = this->array[this->first_free].next;
    this->array[this->first_free].info = e; // we add it to the end
    this->array[this->first_free].next = -1;
    this->array[this->first_free].prev = this->tail;

    if (this->tail != -1)
        this->array[this->tail].next = this->first_free; // we relink the end

    this->tail = this->first_free; // we modify the tail

    if (this->length == 0) // if necessary we create the new head
        this->head = this->first_free;

    this->length++; // we update the length

    this->first_free = copy;

    if (this->length >= this->capacity) { // if there are none, we resize the array
        this->capacity *= 2;
        auto *new_arr = new DLLANode[this->capacity];
        for (int i = 0; i < this->length; i++) {
            new_arr[i] = this->array[i];
        }
        for (int i = this->length; i < this->capacity; i++) {
            new_arr[i].next = new_arr[i].prev = new_arr[i].info = NULL_TELEM;
        }
        delete[] this->array;
        this->array = new_arr;
    }
}

/// BC: theta(1) (throws exception)
/// WC: theta(2*length+capacity) (last element, resize and last free)
/// AC: O(capacity)
void IndexedList::addToPosition(int pos, TElem e) {
    if (pos > this->length)
        throw std::exception();

    auto current = this->head;
    auto counter = 0;

    while (counter != pos or current != -1) {  // checking the validity of the position
        if (counter == pos)
            break;
        else {
            current = this->array[current].next;
            counter++;
        }
    }

    if (current == -1) // if not a valid position
        throw std::exception();


    if (this->first_free == -1) { // we search for the first free space in the array

        if (this->length >= this->capacity) { // if there are none, we resize the array
            this->capacity *= 2;
            auto *new_arr = new DLLANode[this->capacity];
            for (int i = 0; i < this->length; i++) {
                new_arr[i] = this->array[i];
            }
            for (int i = this->length; i < this->capacity; i++) {
                new_arr[i].next = new_arr[i].prev = new_arr[i].info = NULL_TELEM;
            }
            delete[] this->array;
            this->array = new_arr;
        }

       this->initFreeSpace();
    }
    // counter == pos in array, current = pos in DLL

    int copy = this->array[this->first_free].next;
    this->array[first_free].info = e; // we add the TElem on the position

    /// RELINKING
    if (current == this->head) { // if we add to the first position

        if (this->length == 0) { // if the array is empty
            this->array[first_free].next = this->array[first_free].prev = -1;
            this->head = this->tail = this->first_free;
        } else { // if the array is not empty
            this->array[first_free].prev = -1;
            this->array[first_free].next = this->head;

            this->array[this->head].prev = this->first_free;

            this->head = this->first_free;
        }
    } else { // if we add to any other position in the array
        // 1 -> 2
        // 1 -> 3 -> 2
        //     ff   current
        this->array[first_free].prev = this->array[current].prev;
        this->array[first_free].next = current;

        this->array[this->array[current].prev].next = first_free;
        this->array[current].prev = first_free;
    }

    this->first_free = copy;

    this->length++;
}

/// BC: theta(1) (throws exception)
/// WC: theta(length) (last element)
/// AC: O(length)
TElem IndexedList::remove(int pos) {
    auto current = this->head;
    auto counter = 0;
    auto copy = NULL_TELEM;

    if (pos > this->length)
        throw std::exception();

    while (counter != pos or current != -1) {  // checking the validity of the position
        if (counter == pos)
            break;
        else {
            current = this->array[current].next;
            counter++;
        }
    }

    if (current == -1) // if not a valid position
        throw std::exception();

    copy = this->array[current].info;
    this->array[current].info = NULL_TELEM; // removing the element

    /// RELINKING
    if (current == this->head) { // if we remove the first element
        if (this->length == 1) { // if it's the only element to be removed

            this->head = -1;
            this->tail = -1;
        } else { // if it's the head but there are other elements
            this->array[this->array[current].next].prev = -1; // relink the new head

            this->head = this->array[current].next; // change the head

        }
    } else {
        if (current == this->tail) { // if we remove the tail
            this->array[this->array[current].prev].next = -1; // relink the new tail

            this->tail = this->array[current].prev; // change the tail

        } else { // if it's a random element
            this->array[this->array[current].prev].next = this->array[current].next;
            this->array[this->array[current].next].prev = this->array[current].prev;
        }
    }

    this->array[current].prev = this->array[current].next = NULL_TELEM; // removing the next and prev

    this->initFreeSpace();

    this->length--;

    return copy;

}

/// BC: theta(1) (first element)
/// WC: theta(length) (last element or nonexistent)
/// AC: O(length)
int IndexedList::search(TElem e) const {
    int current = this->head;
    int counter = 0;
    while (current != -1) {
        if (this->array[current].info == e)
            return counter;
        current = this->array[current].next;
        counter++;
    }
    return -1;
}

/// BC: theta(1)
/// WC: theta(1)
/// AC: O(1)
ListIterator IndexedList::iterator() const {
    return ListIterator(*this);
}

/// BC: theta(1)
/// WC: theta(1)
/// AC: O(1)
IndexedList::~IndexedList() {
    delete[] this->array;
}

/// BC: theta(1) (throws exception)
/// WC: theta((end-start)*length)
/// AC: O((end-start)*length)
void IndexedList::removeBetween(int start, int end) {

    if (start > this->length or end < 0 or end > this->length or start < 0 or start>end)
        throw std::exception();

    for(int i=start; i<=end; i++)
        this->remove(start);

}

void IndexedList::initFreeSpace() {
    for(int i=0; i<this->capacity; i++)
        if(this->array[i].info == NULL_TELEM and this->first_free == -1) { // finding the first free and making it the head
            this->first_free = i;
            this->array[i].prev = -1;
            this->array[i].next = -1;
        }

    int c = this->first_free;

    for(int i = this->first_free; i<this->capacity; i++){
        if(this->array[i].info == NULL_TELEM and c != this->first_free){
            this->array[c].next = i; // link previous
            this->array[i].prev = c;
            this->array[i].next = -1;
            c = i;
        }
    }
}
