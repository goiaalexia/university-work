#include "action.h"


void RemoveAction::executeRedo() {
    this->r.removeSong(this->removedSong);
}

void RemoveAction::executeUndo() {
    this->r.addSong(this->removedSong);
}
AddAction::AddAction(Song s, Repository &repo) : r(repo) {
    this->addedSong = s;
}

void AddAction::executeUndo() {
    this->r.removeSong(this->addedSong);
}

void AddAction::executeRedo() {
    this->r.addSong(this->addedSong);
}

RemoveAction::RemoveAction(Song s, Repository &repo) : r(repo) {
    this->removedSong = s;
}

UpdateAction::UpdateAction(Song s1, Song s2, Repository& r) : r{r} {
    this->beforeSong = s1;
    this->afterSong = s2;

}
void UpdateAction::executeUndo() {
    this->r.addSong(this->beforeSong);
    this->r.removeSong(this->afterSong);
}

void UpdateAction::executeRedo() {
    this->r.removeSong(this->beforeSong);
    this->r.addSong(this->afterSong);
}