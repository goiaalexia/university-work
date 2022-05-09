#include "header files/MultiMapIterator.h"
#include "header files/MultiMap.h"


MultiMapIterator::MultiMapIterator(const MultiMap &c) : col(c) {
    if (c.isEmpty()) {
        this->current = nullptr;
    } else {
        this->current = c.head;
    }
}

TElem MultiMapIterator::getCurrent() const {
if(valid())
    return make_pair(this->current->info, this->current->v->info);
throw exception();
}

bool MultiMapIterator::valid() const {
    if (this->current != nullptr)
        return true;
    return false;
}

void MultiMapIterator::next() {
    if(valid()){
    if (this->current->v->next != nullptr) {
        this->current->v = this->current->v->next;
    } // if we still have values
    else { // if no more values
        this->current = this->current->next;
    }}
    else
        throw exception();
}

void MultiMapIterator::first() {
    this->current = this->col.head;
}

