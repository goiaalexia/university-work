#pragma once

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM 0

class Matrix {

private:
    TElem *values;
    TElem *lines;
    TElem *cols;
    int length;
    int capacity;
    int lenLines;
    int lenCols;

public:
    //constructor
    Matrix(int nrLines, int nrCols);

    //destructor
    ~Matrix();

    // copy constructor
    Matrix(Matrix &M);
    //returns the number of lines
    /// BC: theta(1)
    /// WC: theta(1)
    /// AC: theta(1)
    int nrLines() const { return this->lenLines; };

    //returns the number of columns
    /// BC: theta(1)
    /// WC: theta(1)
    /// AC: O(1)
    int nrColumns() const { return this->lenCols; };

    //returns the element from line i and column j (indexing starts from 0)
    //throws exception if (i,j) is not a valid position in the Matrix
    /// BC: theta(1) (first element)
    /// WC: theta(n) (last element)
    /// AC: O(n)
    TElem element(int i, int j) const;

    //modifies the value from line i and column j
    //returns the previous value from the position
    //throws exception if (i,j) is not a valid position in the Matrix
    /// BC: theta(1) (first element)
    /// WC: theta(n) (last element)
    /// AC: O(n)
    TElem modify(int i, int j, TElem e);

    //transforms the current matrix into its own transposed (element from position i,j becomes
    // element on position j, i)

    void transpose();

};
