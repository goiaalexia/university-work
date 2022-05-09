#include "header files/Matrix.h"
#include <exception>
#include <iostream>

using namespace std;

/// <summary>
/// BC: theta(1)
/// WC: theta(1)
/// AC: O(1)
/// </summary>
/// <returns></returns>
Matrix::Matrix(int nrLines, int nrCols) {

    this->capacity = 10;
    this->values = new TElem[this->capacity]; // actual storage
    this->lenCols = nrCols; // no. of columns
    this->lenLines = nrLines; // no. of lines
    this->cols = new int[this->lenCols]; // indexes
    this->lines = new int[this->lenLines]; // indexes
    this->length = 0; // no. of elements
}

Matrix::Matrix(Matrix &M) {
    this->capacity = M.capacity;
    this->values = M.values;
    this->lenCols = M.lenCols;
    this->lenLines = M.lenLines;
    this->cols = M.cols;
    this->lines = M.lines;
    this->length = M.length;

}

Matrix::~Matrix() {
    delete[] this->values;
    delete[] this->cols;
    delete[] this->lines;
}


TElem Matrix::element(int i, int j) const {

    if (i < 0 || i > this->lenLines || j < 0 || j > this->lenCols)
        throw exception();

    for (int c = 0; c < this->length; c++) {
        if (this->lines[c] == i && this->cols[c] == j) {
            return this->values[c];
        }
    }
    return NULL_TELEM;
}


TElem Matrix::modify(int i, int j, TElem e) {

    if (i < 0 || i > this->lenLines || j < 0 || j > this->lenCols)
        throw exception();

    int k;
    TElem prev = element(i, j); // previous element

    if (prev != NULL_TELEM) { // if we have an element there
        if (e == NULL_TELEM) { // if we want to delete it
            int pos = -1;
            for (k = 0; k < this->length; k++) {
                if (this->lines[k] == i && this->cols[k] == j) {
                    pos = k;
                }
            }
            //if(pos==-1)
            for (k = pos; k <= this->length - 2; k++) {
                this->lines[k] = this->lines[k + 1];
                this->cols[k] = this->cols[k + 1];
                this->values[k] = this->values[k + 1];
            }
            this->length--;
        } else {
            for (k = 0; k < this->length; k++) {
                if (this->lines[k] == i && this->cols[k] == j) {
                    this->values[k] = e; // we find it and modify it
                }
            }
        }
    } else { // if we don't have an element there
        if (this->capacity == this->length) { // if we have no space left to add it, we resize the matrix
            this->capacity *= 2;
            auto *aux_lines = new TElem[this->capacity];
            auto *aux_cols = new TElem[this->capacity];
            auto *aux_values = new TElem[this->capacity];
            for (k = 0; k < this->length; k++) {
                aux_lines[k] = this->lines[k];
                aux_cols[k] = this->cols[k];
                aux_values[k] = this->values[k];
            }
            delete[] this->lines;
            delete[] this->cols;
            delete[] this->values;
            this->lines = aux_lines;
            this->cols = aux_cols;
            this->values = aux_values;
        }
        this->length++; // we add it
        int pos = 0;
        for (k = 0; k < this->length; k++) {
            if (this->lines[k] == i && this->cols[k] == j) {
                pos = k + 1;
                break;
            }
        }
        for (k = this->length - 1; k >= pos; k--) {
            this->lines[k] = this->lines[k - 1];
            this->cols[k] = this->cols[k - 1];
            this->values[k] = this->values[k - 1];
        }
        this->lines[pos] = i;
        this->cols[pos] = j;
        this->values[pos] = e;


        /*
        for (k = 0; k < this->length; k++) {
            cout << lines[k] << " ";
        }
        cout << endl;
        for (k = 0; k < this->length; k++) {
            cout << cols[k] << " ";
        }
        cout << endl;
        for (k = 0; k < this->length; k++) {
            cout << values[k] << " ";
        }
        cout << endl;
        cout << endl;
    */}

    return prev;
}

void Matrix::transpose() {
    int swap;
    for (int i = 0; i < this->length; i++) {
        swap = this->lines[i];
        this->lines[i] = this->cols[i];
        this->cols[i] = swap;
    }
}





