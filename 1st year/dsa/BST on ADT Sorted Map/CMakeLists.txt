cmake_minimum_required(VERSION 3.16)
project(Sorted_Map)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Sorted_Map
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        ShortTest.cpp
        ShortTest.h
        SMIterator.cpp
        SMIterator.h
        SortedMap.cpp
        SortedMap.h)
