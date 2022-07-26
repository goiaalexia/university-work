#pragma once
#include "MultiMap.h"

class MultiMap;

class MultiMapIterator
{
    friend class MultiMap;

private:
    MultiMap map;
    int indexKey = -1;
    int indexValue = -1;


    MultiMapIterator(const MultiMap& m);


public:
    TElem getCurrent()const;
    bool valid() const;
    void next();
    void first();
    ~MultiMapIterator();
};