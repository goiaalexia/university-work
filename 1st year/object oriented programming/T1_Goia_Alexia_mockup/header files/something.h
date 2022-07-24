#include <string>

#pragma once

class Dick {
private:
    int length;
    int width;
    std::string name;
public:
    Dick() : length{0}, width{0}, name{""} {};

    Dick(int length, int width, const std::string &name);

    int get_length() { return this->length; };

    int get_width() { return this->width; };

    std::string const get_name() { return this->name; };

    void update(int length, int width, const std::string &name);

    std::string to_string();
};