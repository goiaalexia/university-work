#pragma once
#include "IndexedList.h"


class ListIterator{
    //DO NOT CHANGE THIS PART
	friend class IndexedList;
private:
	const IndexedList& list;
	int current;

public:
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;

    explicit ListIterator(const IndexedList& list);
};

