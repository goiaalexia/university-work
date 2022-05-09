//
// Created by lexig on 02.05.2022.
//

#include "../headers/person.h"

void Person::addMeasurement(Measurement *m) {
    this->repo.push_back(m);
}

std::vector<Measurement *> Person::getAllMeasurements() {
    return this->repo;
}

std::vector<Measurement *> Person::getMeasurementsByMonth(int month) {
    std::vector<Measurement*> k;
    for(auto i: this->repo){
        int c;
        if(i->date[5] == 0)
            c =  i->date[6];
        else
            c = i->date[5]*10 + i->date[6];

        if(c == month and c-1>0) // ?
            k.push_back(i);
    }
    return k;
}
