cmake_minimum_required(VERSION 3.16)
project(oldbuildings_test_practice)

set(CMAKE_CXX_STANDARD 14)

add_executable(oldbuildings_test_practice main.cpp headers/buildings.h source/service.cpp headers/service.h source/buildings.cpp headers/repo.h headers/ui.h)
