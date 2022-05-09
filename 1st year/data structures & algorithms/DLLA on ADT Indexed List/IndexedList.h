#pragma once
//DO NOT INCLUDE LISTITERATOR

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM (-11111)
struct DLLANode
{
    TElem info;
    int next;
    int prev;
};

class ListIterator;

class IndexedList {
private:
    DLLANode* array;
    int capacity;
    int head;
    int tail;
    int first_free;
    int length;

	
	//DO NOT CHANGE THIS PART
    friend class ListIterator;
public:
    // constructor
    IndexedList ();

    // returns the number of elements from the list
    int size() const;

    // checks if the list is empty
    bool isEmpty() const;

    // returns an element from a position
    //throws exception if the position is not valid
    TElem getElement(int pos) const;

    // modifies an element from a given position
	//returns the old value from the position
    //throws an exception if the position is not valid
    TElem setElement(int pos, TElem e);

    // adds an element to the end of the list
    void addToEnd(TElem e);

    // adds an element to a given position
    //throws an exception if the position is not valid
    void addToPosition(int pos, TElem e);

    // removes an element from a given position
	//returns the removed element
    //throws an exception if the position is not valid
    TElem remove(int pos);

    // searches for an element and returns the first position where the element appears or -1 if the element is not in the list
    int search(TElem e)  const;

    // returns an iterator set to the first element of the list or invalid if the list is empty
    ListIterator iterator() const;

    void removeBetween(int start, int end);

    void initFreeSpace();

    //destructor
    ~IndexedList();

};
