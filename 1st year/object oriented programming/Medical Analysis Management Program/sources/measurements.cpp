//
// Created by lexig on 02.05.2022.
//

#include "../headers/measurements.h"

#include <utility>

Measurement::Measurement() {

}

Measurement::~Measurement() {

}

BMI::BMI() {

}

BMI::~BMI() {

}

bool BMI::isNormalValue() {
    return 18.5 <= this->value and this->value <= 25;
}

std::string BMI::to_string() {
    std::string f;
    f += "BP " + this->date + "  value: " + std::to_string(this->value) + "\n";
    return f;
}

BMI::BMI(double val, std::string data) {
    this->value = val;
    this->date = std::move(data);
}

BP::BP() = default;

BP::~BP() = default;

bool BP::isNormalValue() {
    return (90 <= this->systolic) and (this->systolic <= 119) and (60 <= this->diastolic) and (this->diastolic <= 79);
}

std::string BP::to_string() {
    std::string f;
    f += "BP " + this->date + "  sys: " + std::to_string(this->systolic) + "  dias: " + std::to_string(this->diastolic)+ "\n";
    return f;
}

BP::BP(int sys, int dia, std::string data) {
    this->diastolic = dia;
    this->systolic = sys;
    this->date = std::move(data);
}
