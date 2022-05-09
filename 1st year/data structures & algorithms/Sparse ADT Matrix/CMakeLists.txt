cmake_minimum_required(VERSION 3.16)
project(Matrix)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Matrix
        App.cpp
        ExtendedTest.cpp
        "header files/ExtendedTest.h"
        Matrix.cpp
        "header files/Matrix.h"
        ShortTest.cpp
        "header files/ShortTest.h")
