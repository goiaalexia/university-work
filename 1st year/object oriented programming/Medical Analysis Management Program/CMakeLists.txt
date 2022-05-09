cmake_minimum_required(VERSION 3.16)
project(medicalstuff_test_practice)

set(CMAKE_CXX_STANDARD 14)

add_executable(medicalstuff_test_practice main.cpp headers/ui.h sources/measurements.cpp headers/measurements.h sources/person.cpp headers/person.h)
