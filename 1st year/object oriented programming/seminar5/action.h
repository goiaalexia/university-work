#pragma once
#include <utility>

#include "Repository.h"

class Action {
public:
    virtual void executeUndo() = 0;
    virtual void executeRedo() = 0;
    virtual ~Action() = default;
};

class AddAction : public Action {
private:
    Repository &r;
    Song addedSong;
public:
    AddAction(Song s, Repository &repo);
    void executeUndo() override;
    void executeRedo() override;
};


class RemoveAction : public Action {
private:
    Repository &r;
    Song removedSong;
public:
    RemoveAction(Song s, Repository &repo);
    void executeUndo() override;
    void executeRedo() override;
};

class UpdateAction : public Action {
private:
    Repository &r;
    Song beforeSong, afterSong;
public:
    UpdateAction(Song s1, Song s2, Repository &repo);
    void executeUndo() override;
    void executeRedo() override;
};