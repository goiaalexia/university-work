cmake_minimum_required(VERSION 3.21)
project(Lecture6_demo_abstract_classes)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Lecture6_demo_abstract_classes
        Animal.cpp
        Animal.h
        Dog.cpp
        Dog.h
        Filter.h
        main.cpp
        Penguin.cpp
        Penguin.h
        Zoo.cpp
        Zoo.h)
