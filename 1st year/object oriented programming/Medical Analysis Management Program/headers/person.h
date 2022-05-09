#pragma once
#include "measurements.h"
#include <vector>


class Person{
public:
    std::string name;
    std::vector<Measurement*> repo;

    void addMeasurement(Measurement* m);
    std::vector<Measurement*> getAllMeasurements();
    std::vector<Measurement*> getMeasurementsByMonth(int month);
};