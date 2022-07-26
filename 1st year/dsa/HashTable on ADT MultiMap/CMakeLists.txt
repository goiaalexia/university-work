cmake_minimum_required(VERSION 3.16)
project(MultiMap__1_)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(MultiMap__1_
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        MultiMap.cpp
        MultiMap.h
        MultiMapIterator.cpp
        MultiMapIterator.h
        ShortTest.cpp
        ShortTest.h)
