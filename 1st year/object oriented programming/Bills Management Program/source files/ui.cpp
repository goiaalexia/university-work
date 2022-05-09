#include <iostream>
#include "../header files/repo.h"
#include "../header files/ui.h"
#include <cstdlib>

UI::UI(Service service) : service{service} {

}

void print_menu() {
    std::cout << "0. Exit\n";
    std::cout << "1. Remove bill\n";
    std::cout << "2. Show all bills\n";
    std::cout << "3. Sort by due date\n";
    std::cout << "4. Total unpaid bills\n";
}

int get_command() {
    int c;
    std::cout << "Input command:";
    std::cin >> c;
    return c;
}

void UI::generate() {
    for (int i = 1; i <= 5; i++) {
        this->service.add_to_repo(std::to_string(i),std::to_string(i),std::to_string(i),float(i),true);
    }

}

void UI::start_ui() {
    bool run = true;
    std::string serial_number, due="06.04.2022";
    generate();
    int command;
    while (run) {
        print_menu();
        command = get_command();
        switch (command) {
            case 0:
                run = false;
                std::cout << "Goodbye!\n";
                break;
            case 1: {
                std::cout << "Please enter the bill's serial number:";
                std::cin >> serial_number;
                if (!this->service.get_repo().find(serial_number)) {
                    std::cout << "No bill with that serial number!\n";
                    break;
                } else {
                    this->service.remove_from_repo(
                            this->service.search_in_repo(serial_number).get_at(0).get_due_date());
                    std::cout << "Bill removed!\n";
                }
                break;
            }
            case 2:{
                std::string s;
                for (int i = 0; i < this->service.get_size(); i++) {
                    s += this->service.get_repo().get_at(i).to_string();
                    s += "\n";
                }
                std::cout << s;

                break;}
                case 4: {
                    std::string s;
                    for (int i = 0; i < this->service.get_size(); i++) {
                        if(this->service.get_repo().get_at(i).get_paid() == false){
                        s += this->service.get_repo().get_at(i).to_string();
                        s += "\n";}
                    }
                    std::cout << s;

                    break;
                }
        }

    }

}