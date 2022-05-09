#pragma once
#include "person.h"
#include <fstream>

class UI{
public:
    Person lol;

    void print_menu(){
        std::cout<<"1. add new\n2. list all\n3. is healthy\n 4. file\n0. exit\n";
    }

    int get_option(){
        int opt;
        std::cout<<"Option: ";
        std::cin>>opt;
        return opt;
    }

    void start(){
        bool running = true;
        std::cout<<"name?: ";
        std::cin>>this->lol.name;
        while(running){
            print_menu();
            int option = get_option();
            switch(option){
                case 0:{
                    running = false;
                    std::cout<<"goodbye!";
                    break;}
                case 1:{
                    Measurement* m;
                    std::string date, type;
                    try {
                        std::cout<<"input type: ";
                        std::cin >> type;
                        std::cout<<"input date: ";
                        std::cin>>date;
                        if (type != "BMI" and type != "BP" or date.length() != 10) {
                            throw std::exception();
                        }
                    }
                    catch(std::exception&){
                        std::cout<<"not good!\n\n";
                        break;
                    }
                    if(type == "BMI"){
                        double val;
                        std::cout<<"value: ";
                        std::cin>>val;
                        m = new BMI(val, date);
                        this->lol.addMeasurement(m);
                    }
                    else{
                        int sys, dis;
                        std::cout<<"sys: ";
                        std::cin>>sys;
                        std::cout<<"dia: ";
                        std::cin>>dis;
                        m = new BP(sys, dis, date);
                        this->lol.addMeasurement(m);
                    }
                    if(m->isNormalValue()) std::cout<<"normal!\n\n";
                    else std::cout<<"not normal!\n\n";
                    break;
                }
                case 2:{
                    std::cout<<this->lol.name<<std::endl;
                    for(auto i: this->lol.repo)
                        std::cout<<i->to_string()<<std::endl;
                    break;
                }
                case 4:{
                    std::string name;
                    std::cout<<"file name: ";
                    std::cin>>name;
                    std::string date;
                    std::cout<<"date: ";
                    std::cin>>date;
                    std::ofstream out(name);
                    for(auto i: this->lol.getAllMeasurements())
                        if(date<i->date)
                            out<<i->to_string()<<std::endl;
                    break;
                }
                case 3:{int month;
                    std::cout<<"month: ";
                    std::cin>>month;
                    auto c = true;
                    for(auto i: this->lol.getMeasurementsByMonth(month))
                        if(!i->isNormalValue()){
                            std::cout<<"no!\n";
                            c = false;
                            break;
                        }
                    if(c)
                        std::cout<<"yes!\n";
                    break;
                }
                default:{
                    std::cout<<"invalid option!\n\n";
                    break;

                }


            }

        }
    }
};