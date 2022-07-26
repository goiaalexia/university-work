#include "MultiMapIterator.h"
#include "MultiMap.h"

// BC/AC/WC: Theta(1)
MultiMapIterator::MultiMapIterator(const MultiMap &m) : map(m) {
    this->first();
}


//BC: Theta(1)
//AC/WC: O(1)
TElem MultiMapIterator::getCurrent() const {
    TElem current;
    if (this->indexKey == -1 || this->indexValue == -1 || this->indexKey == this->map.arrayCapacity)
        throw std::exception();
    current.first = this->map.hashtable[this->indexKey].first;
    current.second = this->map.hashtable[this->indexKey].second[indexValue];
    return current;
}

//BC/AC/WC: Theta(1)
bool MultiMapIterator::valid() const {
    if (this->indexKey == -1 || this->indexKey == this->map.arrayCapacity || this->indexValue == -1)
        return false;
    return true;
}


//BC: Theta(1)
//AC: Theta(capacity)
//WC: O(capacity)
void MultiMapIterator::next() {
    if(this->indexKey == -1 || this->indexValue == -1)
        throw std::exception();

    int indexK = this->indexKey;
    int indexV = this->indexValue + 1;

    if (indexV < this->map.hashtable[indexK].second.size()) {
        this->indexValue++;
        return;
    }

    else {
        indexK++;
        while (indexK < this->map.arrayCapacity) {
            if (this->map.hashtable[indexK].first != NULL_TKEY && this->map.hashtable[indexK].first != DELETED_TKEY) {
                this->indexKey = indexK;
                this->indexValue = 0;
                return;
            }
            indexK++;
        }
    }
    this->indexKey = this->map.arrayCapacity;
}

//BC: O(1)
//AC: Theta(capacity)
//WC: O(capacity)
void MultiMapIterator::first() {
    int i = 0;
    while (i < this->map.arrayCapacity) {
        if (this->map.hashtable[i].first != NULL_TKEY && this->map.hashtable[i].first != DELETED_TKEY) {
            this->indexKey = i;
            this->indexValue = 0;
            return;
        }
        i++;
    }
    this->indexKey = -1;
    this->indexValue = -1;
}

MultiMapIterator::~MultiMapIterator() {

}
