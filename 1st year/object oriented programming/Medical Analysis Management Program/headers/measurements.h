#pragma once
#include <iostream>

class Measurement{
public:
    std::string date;

    Measurement();

    virtual ~Measurement() = 0;

    virtual bool isNormalValue() = 0;

    virtual std::string to_string() = 0;


};

class BMI: public Measurement{
public:
    double value;

    BMI();

    BMI(double val, std::string data);

    ~BMI();

    bool isNormalValue() override;

    std::string to_string() override;
};

class BP: public Measurement{
public:
    int systolic;
    int diastolic;

    BP();

    BP(int sys, int dia, std::string data);

    ~BP() override;

    bool isNormalValue() override;

    std::string to_string() override;
};