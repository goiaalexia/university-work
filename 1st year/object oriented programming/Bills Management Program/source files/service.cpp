#include "../header files/service.h"
#include "../header files/bill.h"

Service::Service(Repo &rep) : r{rep} {};

void Service::add_to_repo(std::basic_string<char> serial_no, std::basic_string<char> company,
                          std::basic_string<char> due_date, float sum, bool isPaid) {
    Bill b{serial_no, company, due_date, sum, isPaid};
    this->r.add(b);

}

Repo Service::search_in_repo(const std::string &serial_no) {
    Repo thing;
    for (int i = 0; i < this->get_repo().get_size(); i++) {
        if (this->get_repo().get_at(i).get_serial_no().find(serial_no) != std::string::npos)
            thing.add(this->get_repo().get_at(i));
    }
    return thing;
}


void Service::remove_from_repo(const std::string &serial_no) {
    Bill b = Bill();
    b.set_serial_no(serial_no);
    this->r.remove(b);
}