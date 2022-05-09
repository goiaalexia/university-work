#pragma once
#include "../headers/buildings.h"
#include <vector>
#include <fstream>

class Service{
public:
    std::vector<Building*> repo;

    void addBuilding(Building *b);
    std::vector<Building *> getAllBuildings() const;
    std::vector<Building*> getAllToBeRestored();
    std::vector<Building*> getAllToBeDemolished();
    static void writeToFile(const std::string& fileName, const std::vector<Building*>& buildings);
    void to_string();

    ~Service();
};