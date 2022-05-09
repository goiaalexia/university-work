#include <iostream>
#include "../headers/service.h"

class UI {
private:
    Service serv;
public:

    static void menu(){
        std::cout<<"1. add building\n2. show buildings\n3. show buildings restored\n4. write to file demolish\n5. write to file rebuild\n6. exit\n";
    }
    static int get_option() {
        int option;
        std::cout<<"option:";
        std::cin >> option;
        return option;
    }

    void start() {
        auto* pula = new House("strada M. Kogalniceanu", 2002, true);
        auto* pizda = new Block("strada Lol", 1970, 2000, 1000);
        auto* coaie = new House("strada Slay", 1865, false);
        this->serv.addBuilding(pula);
        this->serv.addBuilding(pizda);
        this->serv.addBuilding(coaie);
        bool running = true;
        while (running) {
            menu();
            int opt = get_option();
            switch (opt) {
                case 1: {
                    Building* b;
                    int type;
                    std::string addr;
                    int yr;
                    std::cout << "Enter building type (house - 1, flats - 2): ";
                    std::cin >> type;
                    std::cout << "address: ";
                    std::cin >> addr;
                    std::cout << "year: ";
                    std::cin >> yr;
                    if (type == 1) {
                        std::cout << "is historical? (y/n)";
                        std::string isIt;
                        bool is;
                        std::cin >> isIt;
                        if (isIt == "y")
                            is = true;
                        else
                            is = false;
                        b = new House(addr, yr, is);
                    } else {
                        int total, occ;
                        std::cout << "total apts: ";
                        std::cin >> total;
                        std::cout << "occupied: ";
                        std::cin >> occ;
                        b = new Block(addr, yr, total, occ);
                    }
                    this->serv.addBuilding(b);
                    break;
                }
                case 2:{
                    for(auto i: this->serv.getAllBuildings())
                        std::cout<<i->to_string()<<std::endl;
                    break;
                }
                case 3:{
                    int y;
                    std::cout<<"year: ";
                    std::cin>>y;
                    for(auto i: this->serv.getAllToBeRestored())
                        if(i->year > y)
                        std::cout<<i->to_string()<<std::endl;
                    break;
                }
                case 4:{
                    this->serv.writeToFile("destroy.txt", this->serv.getAllToBeDemolished());
                    break;
                }
                case 5:{
                    this->serv.writeToFile("rebuild.txt", this->serv.getAllToBeRestored());
                    break;
                }
                case 6:{
                    std::cout<<"goodbye!";
                    running = false;
                    break;
                }
                default: {
                    std::cout<<"invalid option!\n";
                    break;
                }

            }
        }
    }
};