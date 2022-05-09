#pragma once

#include <cstdlib>

template<class element>
class DynamicArray {
public:
    DynamicArray(); // constructor
    DynamicArray(const DynamicArray &a); // copy constructor
    ~DynamicArray(); // destructor
    DynamicArray &operator=(const DynamicArray &a); // assignment operator

    element &operator[](unsigned int index); // get array item
    void add(const element &item); // Add item to the end of array

    unsigned int get_size(); // get size of array (elements)
    void clear(); // clear array
    void remove(unsigned int pos); // delete array item
    void *get_arr(); // get void* pointer to array data

private:
    element *array; // pointer for array's memory
    unsigned int size; // current element
    unsigned int capacity; // actual size of allocated memory

    const static unsigned int default_capacity = 2;
};

template<class element>
DynamicArray<element>::DynamicArray() : size{0}, capacity{default_capacity} {
    this->array = new element[this->capacity];
}

template<class element>
DynamicArray<element>::DynamicArray(const DynamicArray &a) {
    this->size = a.size;
    this->capacity = a.capacity;
    this->array = new element[this->capacity];
    for (int i = 0; i < this->size; i++)
        this->array[i] = a.array[i];
}

template<class element>
DynamicArray<element>::~DynamicArray() {
    delete[] this->array;
}

template<class element>
DynamicArray<element> &DynamicArray<element>::operator=(const DynamicArray &a) {
    if (this == &a)
        return *this;

    this->capacity = a.capacity;
    this->size = a.size;

    delete[] this->array;
    this->array = new element[this->capacity];
    for (int i = 0; i < this->size; i++)
        this->array[i] = a.array[i];

    return *this;
}

template<class element>
element &DynamicArray<element>::operator[](unsigned int index) {
    return this->array[index];
}

template<class element>
void DynamicArray<element>::add(const element &item) {
    this->size++;
    if (this->size >= this->capacity) {
        this->capacity *= 2;
        element *new_arr = new element[this->capacity];
        for (int i = 0; i < this->size; i++) {
            new_arr[i] = this->array[i];
        }
        delete[] this->array;
        this->array = new_arr;
    }
    this->array[this->size - 1] = item;
}

template<class element>
unsigned int DynamicArray<element>::get_size() {
    return this->size;
}

template<class element>
void DynamicArray<element>::clear() {
    this->size = 0;
    this->capacity = default_capacity;
    delete[] this->array;
    this->array = new element[default_capacity];
}

template<class element>
void DynamicArray<element>::remove(unsigned int pos) {
    //delete this->array[pos];
    for (unsigned int i = pos; i < this->size - 1; i++) {
        this->array[i] = this->array[i + 1];
    }
    this->size--;
}

template<class element>
void *DynamicArray<element>::get_arr() {
    return this->array;
}