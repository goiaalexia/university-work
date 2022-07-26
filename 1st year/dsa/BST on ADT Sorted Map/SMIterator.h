#pragma once
#include "SortedMap.h"

//DO NOT CHANGE THIS PART

class Stack {
private:
    BSTNode** elements;
    int nrElements;
    int capacity;
public:
    Stack();
    int getNrElements() const;
    void push(BSTNode* element);
    void resize();
    TElem operator[](int position) const;
    ~Stack();
};

class SMIterator{
	friend class SortedMap;
private:
	const SortedMap& map;
	SMIterator(const SortedMap& mapionar);
    Stack stack{};
    int current;

public:
	void first();
	void next();
	bool valid() const;
    TElem getCurrent() const;
    void inOrderRecursive(BSTNode* startNode);
};

