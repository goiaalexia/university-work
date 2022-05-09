#pragma once

#include "dynamicArray.h"
#include <string>
#include "bill.h"

class Repo {
private:
    DynamicArray<Bill> data;
public:
    void remove(const Bill &b);
    void add(const Bill &b);
    bool find(const std::string &serial_no);


    unsigned int get_size() { return this->data.get_size(); }

    int get_index(const std::string &serial_no);

    Bill &get_at(int index);

};