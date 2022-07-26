#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

/// ADT  MultiMap – using  a  hashtable  with  open  addressing and  double  hashing
/// in which unique keys are stored with a dynamic array of the associated values.

using namespace std;

//BC/AC/WC: Theta(capacity)
MultiMap::MultiMap() {
    this->arrayCapacity = 2;
    this->arraySize = 0;
    this->hashtable = new TElemArr[this->arrayCapacity];
    for (int i = 0; i < this->arrayCapacity; i++) {
        this->hashtable[i].first = NULL_TKEY;
    }
}

//BC: Theta(1) (empty hashtable)
//AC: Theta(size)
//WC: Theta(keys)
void MultiMap::add(TKey c, TValue v) {
    int i = 0;
    int index = h(c, i);

    // haven't reached the end for i and the key is valid
    while (i < this->arrayCapacity && this->hashtable[index].first != NULL_TKEY
           && this->hashtable[index].first != DELETED_TKEY) {
        if (this->hashtable[index].first == c) { // if we found the key
            this->hashtable[index].second.push_back(v); // we add the value to it
            this->arraySize++; // increment the size
            return;
        }
        i++; // otherwise, we rehash
        index = h(c, i);
    }

    // if we reached the end
    if (i == this->arrayCapacity) {
        this->resize(); // we resize the array
        this->add(c, v); // we try adding it again, it should work now
    } else { // if the slot is empty
        this->hashtable[index].first = c; // we add the new key
        this->hashtable[index].second.push_back(v); // and value
        this->arraySize++;
    }
}

//BC: Theta(1)
//AC: Theta(capacity)
//WC: O(capacity+size)
bool MultiMap::remove(TKey c, TValue v) {
    int i = 0;
    int index = h(c, i);

    // searching the pair until we reach the end, or it is an empty slot
    while (i < this->arrayCapacity && this->hashtable[index].first != NULL_TKEY) {
        if (this->hashtable[index].first == c) // if we found it
        {
            for (int j = 0; j < this->hashtable[index].second.size(); j++) // we go through the values
                if (this->hashtable[index].second[j] == v) { // if we found the value
                    this->hashtable[index].second.erase(this->hashtable[index].second.begin() + j); // we delete it
                    this->arraySize--;

                    if (this->hashtable[index].second.size() == 0) // if we have no more values in that key
                        this->hashtable[index].first = DELETED_TKEY;
                    return true; // delete successful
                }
            return false; // when the value does not exist
        }
        i++;
        index = h(c, i); // otherwise we rehash
    }
    return false; // not found, not removed
}

//BC: Theta(1) (empty hashtable)
//AC: Theta(capacity)
// WC: O(capacity)
vector<TValue> MultiMap::search(TKey c) const {
    int i = 0;
    int index = h(c, i);
    //TODO: ask about const reference

    // searching until we either find end or empty slot
    while (i < this->arrayCapacity && this->hashtable[index].first != NULL_TKEY)
    {
        if (this->hashtable[index].first == c) // if we found the key
            return this->hashtable[index].second; // we return the vector
        i++;
        index = this->h(c, i); // keep searching and rehashing lol

    }
    std::vector<TValue> empty;
    return empty; // for when we find nothing
}


//BC/AC/WC: Theta(1)
int MultiMap::size() const {
    return this->arraySize;
}


//BC/AC/WC: Theta(1)
bool MultiMap::isEmpty() const {
    return this->arraySize == 0;
}

//BC/AC/WC: Theta(1)
MultiMapIterator MultiMap::iterator() const {
    return MultiMapIterator(*this);
}





//BC/AC/WC: Theta(2*size + capacity)
void MultiMap::resize() {
    std::vector<TElem> values;

    // copy the elements that were in the hashtable

    for (int i = 0; i < this->arrayCapacity; i++)
        for (auto elem: this->hashtable[i].second) {
            TElem current(this->hashtable[i].first, elem);
            values.push_back(current);
        }

    this->arrayCapacity *= 2;
    this->hashtable = new TElemArr[this->arrayCapacity];
    this->arraySize = 0;

    for (int i = 0; i < this->arrayCapacity; i++) // reinitializing the hashtable
        this->hashtable[i].first = NULL_TKEY;

    for (auto elem: values) // adding the values back to the resized hashtable
        this->add(elem.first, elem.second);
}

//BC: Theta(1)
//AC: Theta(size+capacity)
//WC: Theta(2*(size+capacity))
vector<TValue> MultiMap::removeKey(TKey c) {
    int i = 0;
    int index = h(c, i);
    vector<TValue> vec;

    // searching the key until we reach the end, or it is an empty slot
    while (i < this->arrayCapacity && this->hashtable[index].first != NULL_TKEY) {
        if (this->hashtable[index].first == c) // if we found the key
        {while(!this->hashtable[index].second.empty()) { // we go through the values
                vec.push_back(this->hashtable[index].second[0]); // we retain them
                this->hashtable[index].second.erase(this->hashtable[index].second.begin()); // we delete them
                this->arraySize--;
            }

            this->hashtable[index].first = DELETED_TKEY;
            return vec;
        }
        i++;
        index = h(c, i); // otherwise we rehash
    }
    return vec;
}











MultiMap::~MultiMap() {
    //delete this->hashtable;
}