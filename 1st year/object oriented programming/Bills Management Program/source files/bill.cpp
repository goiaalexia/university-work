#include "../header files/bill.h"

std::string Bill::to_string() {
    std::string s;
    s += this->serial_no + "; " + this->company + "; " + this->due_date + "; " + std::to_string(this->sum) + "; " + std::to_string(this->isPaid) + "\n";
    return s;
}

Bill::Bill(std::string &serial_no, std::string &company, std::string &due_date, double sum, bool isPaid) {
    this->serial_no = serial_no;
    this->company = company;
    this->due_date = due_date;
    this->sum = sum;
    this->isPaid = isPaid;


}
