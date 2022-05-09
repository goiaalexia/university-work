#include "../header files/MultiMap.h"
#include "../header files/MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;

KeyNode *MultiMap::checkKey(TKey key) const {
    KeyNode *current = this->head;
    KeyNode *sol = nullptr;

    while (current != nullptr) {
        if (current->info == key) {
            sol = current;
            return sol;
        }
        current = current->next;
    }

    return sol;
}

void MultiMap::addNewKey(TKey k) {
    auto *node = new KeyNode;

    node->info = k;
    node->v = nullptr;
    node->next = nullptr;

    if (this->head == nullptr) {
        this->head = node;
        this->tail = node;
        return;
    }

    this->tail->next = node;
    this->tail = this->tail->next;
}

void MultiMap::addValueToKey(TKey k, TValue v) {
    KeyNode *currentNodeKey = this->head;

    while (currentNodeKey != nullptr && currentNodeKey->info != k) {
        currentNodeKey = currentNodeKey->next;
    }

    auto *nodeVal = new ValueNode;
    nodeVal->info = v;
    nodeVal->next = nullptr;

    if (currentNodeKey->v == nullptr) {
        currentNodeKey->v = nodeVal;
        return;
    }

    ValueNode *currentNodeValue = currentNodeKey->v;

    while (currentNodeValue->next != nullptr) {
        currentNodeValue = currentNodeValue->next;
    }

    currentNodeValue->next = nodeVal;
}

void MultiMap::freeValues(ValueNode *head) {
    while (head != nullptr) {
        ValueNode *tmp = head;
        head = head->next;
        delete tmp;
    }
}

MultiMap::MultiMap() {
    this->head = nullptr;
    this->tail = nullptr;
    this->length = 0;
}


void MultiMap::add(TKey c, TValue v) {
    KeyNode *key = this->checkKey(c);

    // if the key is not in the multimap
    if (key == nullptr) {
        this->addNewKey(c);
    }

    // add the value
    this->addValueToKey(c, v);

    this->length++;
}


bool MultiMap::remove(TKey c, TValue v) {
    auto currentElem = head;
    KeyNode *previous = nullptr;
    ValueNode *previous_a = nullptr;
    while (currentElem != nullptr and currentElem->info != c) {
        previous = currentElem;
        currentElem = currentElem->next;
    }
    if (currentElem == nullptr) { // if key not found
        return false;
    }

    while (currentElem->v != nullptr and currentElem->v->info != v) {
        previous_a = currentElem->v;
        currentElem->v = currentElem->v->next;
    }

    if (previous_a != nullptr) { // if value found
        if(currentElem->v != nullptr)
            previous_a->next = currentElem->v->next;
        else
            previous_a->next = nullptr;
    } else {
        if(currentElem->v != nullptr)
            currentElem->v = currentElem->v->next;
        else
            currentElem->v = nullptr;
        //currentElem->v = currentElem->v->next;
    }

    if (currentElem->v == nullptr) {
        if (previous != nullptr) {
            previous->next = currentElem->next;
        } else {
            this->head = currentElem->next;
        }
    }

    this->length--;
    return true;
}


vector<TValue> MultiMap::search(TKey c) const {
    vector<TValue> sol;

    KeyNode *node = this->checkKey(c);

    if (node == nullptr) {
        return sol;
    }

    ValueNode *currentValue = node->v;

    while (currentValue != nullptr) {
        sol.push_back(currentValue->info);
        currentValue = currentValue->next;
    }

    return sol;
}


int MultiMap::size() const {
    return this->length;
}


bool MultiMap::isEmpty() const {
    return this->length == 0;
}

MultiMapIterator MultiMap::iterator() const {
    return MultiMapIterator(*this);
}


MultiMap::~MultiMap() {
    while (this->head != nullptr) {
        KeyNode *tmp = this->head;
        this->freeValues(this->head->v);
        this->head = this->head->next;
        delete tmp;
    }
}