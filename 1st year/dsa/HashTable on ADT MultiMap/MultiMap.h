#pragma once

#include<vector>
#include<utility>
#include <cmath>
//DO NOT INCLUDE MultiMapIterator

using namespace std;

//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
typedef std::pair<TKey, std::vector<TValue>> TElemArr;
#define NULL_TVALUE (-111111)
#define NULL_TKEY (-111111)
#define DELETED_TKEY (-111112)
#define DELETED_TVALUE (-111112)
#define NULL_TELEM pair<int,int>(-111111, -111111)

class MultiMapIterator;

class MultiMap {
    friend class MultiMapIterator;

private:
    /// hashtable (array), probe sequence (array), (hash function -> two hash functions), size of array
    TElemArr* hashtable; // hashtable (dynamic array)
    //int *probeSequence; // probe sequence (array)
    int arraySize; // total size of hashtable
    int arrayCapacity; // probe sequence count / occupied slots

    int h1(TKey k) const { return abs(k) % this->arrayCapacity; }

    int h2(TKey k) const { return 1 + abs(k) % (this->arrayCapacity - 1); }

    TKey h(TKey k, int i) const { return (h1(k) + i * h2(k)) % this->arrayCapacity; };

    void resize();

public:
    //constructor
    MultiMap();

    //adds a key value pair to the multimap
    void add(TKey c, TValue v);

    //removes a key value pair from the multimap
    //returns true if the pair was removed (if it was in the multimap) and false otherwise
    bool remove(TKey c, TValue v);

    //returns the vector of values associated to a key. If the key is not in the MultiMap, the vector is empty
    vector<TValue> search(TKey c) const;

    //returns the number of pairs from the multimap
    int size() const;

    //checks whether the multimap is empty
    bool isEmpty() const;

    //returns an iterator for the multimap
    MultiMapIterator iterator() const;

    //destructor
    ~MultiMap();

    vector<TValue> removeKey(TKey c);


};

