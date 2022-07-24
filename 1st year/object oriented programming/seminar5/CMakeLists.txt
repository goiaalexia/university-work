cmake_minimum_required(VERSION 3.16)
project(seminar5)

set(CMAKE_CXX_STANDARD 14)

include_directories()

add_executable(
        CSVPlaylist.h
        CSVPlaylist.cpp
        FilePlaylist.cpp
        FilePlaylist.h
        main.cpp
        PlayList.cpp
        PlayList.h
        Repository.cpp
        Repository.h
        RepositoryExceptions.cpp
        RepositoryExceptions.h
        Service.cpp
        Service.h
        Song.cpp
        Song.h
        SongValidator.cpp
        SongValidator.h
        UI.cpp
        UI.h
        Utils.cpp
        Utils.h
        Songs.txt
        action.h
        action.cpp
)