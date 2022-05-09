#pragma once

#include "repo.h"
#include "bill.h"
#include <string>

class Service {

public:
    Repo &r;

    Service(Repo &rep);

    /// THE FUNCTION THAT REMOVES A BILL FROM THE REPO BASED ON ITS SERIAL NUMBER
    /// \param serial_no: the serial number we are searching for
    void remove_from_repo(const std::string &serial_no);

    void
    add_to_repo(std::basic_string<char> serial_no, std::basic_string<char> company, std::basic_string<char> due_date,
                float sum, bool isPaid);

    Repo search_in_repo(const std::string &due_date);

    unsigned int get_size() const { return this->r.get_size(); }

    Repo &get_repo() { return this->r; }
};



