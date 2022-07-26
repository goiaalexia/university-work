#pragma once

#include "SortedMultiMap.h"


class SMMIterator{
    friend class SortedMultiMap;
private:
    //DO NOT CHANGE THIS PART
    const SortedMultiMap& map;
    explicit SMMIterator(const SortedMultiMap& map);
    SortedMultiMap::SMMNode* currentKey;
    SortedMultiMap::IteratorSLLList itList;

public:
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;
};