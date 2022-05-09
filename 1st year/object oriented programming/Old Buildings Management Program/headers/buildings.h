#pragma once

#include <iostream>
#include <cstring>

class Building {
public:
    Building();

    virtual bool mustBeRestored() = 0;

    virtual bool canBeDemolished() = 0;

    virtual std::string to_string();

    virtual ~Building();

    int year;
    std::string address;
};

class Block : public Building {
private:
    int totalApartments;
    int occupiedApartments;
public:
    Block();

    Block(std::string ad, int yr, int tot, int occ);

    bool mustBeRestored() override;

    bool canBeDemolished() override;

    std::string to_string() override;

    ~Block() override;

};

class House : public Building {
private:
    bool isHistorical;
public:
    House();

    House(std::string ad, int yr, bool is);

    bool mustBeRestored() override;

    bool canBeDemolished() override;

    std::string to_string() override;

    ~House() override;
};