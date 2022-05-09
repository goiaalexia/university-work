#include "../headers/buildings.h"
#include "../headers/service.h"



void Service::addBuilding(Building *b) {
    this->repo.push_back(b);

}

std::vector<Building *> Service::getAllBuildings() const {
    return this->repo;
}

std::vector<Building*> Service::getAllToBeRestored() {
    std::vector<Building*> yes;
    for(auto i: this->repo){
        if(i->mustBeRestored())
            yes.push_back(i);
    }
    return yes;
}

std::vector<Building*> Service::getAllToBeDemolished() {
    std::vector<Building*> yes;
    for(auto i: this->repo){
        if(i->canBeDemolished())
            yes.push_back(i);
    }
    return yes;
}

void Service::writeToFile(const std::string& fileName, const std::vector<Building*>& buildings) {
    std::ofstream g(fileName);
    for(auto i: buildings){
        g<<i->to_string()<<std::endl;
    }
    g.close();
}

void Service::to_string() {
    for(auto i: this->repo){
        std::cout<<i->to_string()<<std::endl;
    }

}

Service::~Service() {
    for(auto i: this->repo)
        delete i;
}


