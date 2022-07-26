cmake_minimum_required(VERSION 3.16)
project(IndexedList)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(IndexedList
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        IndexedList.cpp
        IndexedList.h
        ListIterator.cpp
        ListIterator.h
        ShortTest.cpp
        ShortTest.h)
