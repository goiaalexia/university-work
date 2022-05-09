#pragma once
#include "service.h"

class UI {
public:
    UI(Service service);

    void start_ui();

private:
    void generate();
    Service service;
};