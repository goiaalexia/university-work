#pragma once
#include <string>



class Bill {
private:
    std::string serial_no;
    std::string company;
    std::string due_date;
    float sum;
    bool isPaid;
public:
    Bill() : serial_no{""}, company{""}, due_date{""}, sum{0.0}, isPaid{false} {};

    Bill(std::string &serial_no, std::string &company, std::string &due_date, double sum, bool isPaid);

    std::string get_serial_no() const { return this->serial_no; };

    std::string get_company() const { return this->company; };

    std::string get_due_date() const { return this->due_date; };

    void set_serial_no(const std::string &serial_no){ this->serial_no = serial_no; };

    float get_sum() { return this->sum; };
    bool get_paid(){return this->isPaid;};

    std::string to_string();
};