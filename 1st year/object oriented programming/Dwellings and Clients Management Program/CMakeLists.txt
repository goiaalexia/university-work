cmake_minimum_required(VERSION 3.16)
project(test2_oop)

set(CMAKE_CXX_STANDARD 14)

add_executable(test2_oop sources/main.cpp headers/ui.h headers/dwelling.h sources/realestate.cpp headers/realestate.h sources/client.cpp headers/client.h)
