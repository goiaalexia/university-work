#include "../header files/repo.h"
bool Repo::find(const std::string &serial_no) {
    for(int i = 0; i < this->get_size(); i++) {
        if(serial_no == this->data[i].get_serial_no()) {
            return true;
        }
    }
    return false;
}

void Repo::remove(const Bill &t) {
    for(int i = 0; i < this->get_size(); i++) {
        if(t.get_serial_no() == this->data[i].get_serial_no()) {
            this->data.remove(i);
            return;
        }
    }
}

Bill &Repo::get_at(int index) {
    return this->data[index];
}


void Repo::add(const Bill &b) {
    this->data.add(b);
}


int Repo::get_index(const std::string &serial_no) {
    for(int i = 0; i < this->get_size(); i++) {
        if(serial_no == this->data[i].get_serial_no()) {
            return i;
        }
    }
    return -1;
}
