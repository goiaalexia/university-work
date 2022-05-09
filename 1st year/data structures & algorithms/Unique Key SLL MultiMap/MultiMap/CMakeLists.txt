cmake_minimum_required(VERSION 3.16)
project(MultiMap)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(MultiMap
        "source files/App.cpp"
        "source files/ExtendedTest.cpp"
        "header files/ExtendedTest.h"
        "source files/MultiMap.cpp"
        "header files/MultiMap.h"
        "source files/MultiMapIterator.cpp"
        "header files/MultiMapIterator.h"
        "source files/ShortTest.cpp"
        "header files/ShortTest.h")
