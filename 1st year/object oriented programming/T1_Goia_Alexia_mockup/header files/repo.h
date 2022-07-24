#pragma once
#include "dynamicArray.h"
#include <string>
#define T int

class Repo {
private:
    DynamicArray<T> data;
public:
    void add(const T &t);
    void remove(const T &t);
    bool find(const std::string &linky);


    unsigned int get_size() { return this->data.get_size(); }
    int get_index(const std::string &link);
    T &get_at(int index);

};