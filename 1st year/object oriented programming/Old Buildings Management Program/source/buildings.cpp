#include "../headers/buildings.h"

#include <utility>

Block::Block() { this->address = ""; this->occupiedApartments = this->totalApartments = this->year = -1;}

Block::Block(std::string ad, int yr, int tot, int occ) {
    this->occupiedApartments = occ;
    this->totalApartments = tot;
    this->year = yr;
    this->address = std::move(ad);
}

bool Block::mustBeRestored() {
    if(2022 - this->year > 40 && 80*this->totalApartments/100 <= this->occupiedApartments)
        return true;
    return false;
}

bool Block::canBeDemolished() {
    return (5*this->totalApartments/100 >= this->occupiedApartments);
}

Block::~Block() = default;

House::House(std::string ad, int yr, bool is) {
    this->address = std::move(ad);
    this->year = yr;
    this->isHistorical = is;

}

bool House::mustBeRestored() {
    if(2022 - this->year > 100)
        return true;
    return false;
}

bool House::canBeDemolished() {
    return(!this->isHistorical);
}

House::House() { this->address = ""; this->isHistorical = false; this->year = -1;

}

std::string House::to_string() {
    std::string f = Building::to_string();
    f += " " + std::to_string(this->isHistorical);
    return f;
}

House::~House() = default;

Building::Building() { this->year = -1; this->address = "";
}

Building::~Building() = default;

std::string Building::to_string() {
    std::string f = std::to_string(this->year) + " " + this->address;
    return f;
}

std::string Block::to_string() {
    std::string f = Building::to_string();
    f += " " + std::to_string(this->totalApartments) + " " + std::to_string(this->occupiedApartments);
    return f;
}

