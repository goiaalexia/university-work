#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

//Theta(nrNodes)
SMIterator::SMIterator(const SortedMap& m) : map(m){
	BSTNode* startNode = m.root;
    this->current = 0;
    this->inOrderRecursive(startNode);
}

//Theta(1)
void SMIterator::first(){
    this->current = 0;
}

//Theta(1)
void SMIterator::next(){
	if(!valid()){
        throw exception();
    }
    this->current++;
}

//Theta(1)
bool SMIterator::valid() const{
    if (this->current >= this->stack.getNrElements()) {
        return false;
    }
    return true;
}

//Theta(1)
TElem SMIterator::getCurrent() const{
	if (!valid()) {
        throw std::exception();
    }
    return this->stack[this->current];
}

//Theta(nrNodes)
void SMIterator::inOrderRecursive(BSTNode *startNode) {
    if (startNode != nullptr) {
        this->inOrderRecursive(startNode->left);
        this->stack.push(startNode);
        this->inOrderRecursive(startNode->right);
    }
}

//Theta(1)
Stack::Stack(): nrElements{0}, capacity{10} {
    this->elements = new BSTNode*[capacity];
}

//Theta(1)
int Stack::getNrElements() const {
    return this->nrElements;
}

//Theta(1)
void Stack::push(BSTNode *element) {
    if (this->nrElements == this->capacity)
        this->resize();
    this->elements[this->nrElements] = element;
    this->nrElements++;
}

//Theta(nrElements)
void Stack::resize() {
    auto** newElements = new BSTNode*[this->capacity * 2];
    int index;
    for (index = 0; index < this->nrElements; ++index) {
        newElements[index] = this->elements[index];
    }
    this->capacity = this->capacity * 2;
    delete [] this->elements;
    this->elements = newElements;
}

//Theta(1)
TElem Stack::operator[](int position) const {
    return this->elements[position]->info;
}

//Theta(1)
Stack::~Stack() {
    delete [] this->elements;
}

