#include "Service.h"
#include <algorithm>
#include "FilePlaylist.h"
#include "RepositoryExceptions.h"

using namespace std;

void Service::addSongToRepository(const std::string& artist, const std::string& title, double minutes, double seconds, const std::string& source)
{
	Song s{ artist, title, Duration{minutes, seconds}, source };
	this->validator.validate(s);
	this->repo.addSong(s);
    if(this->stack.size() != this->current_undo) {
        this->stack.erase(this->stack.begin()+this->current_undo, this->stack.end());
    }
    this->current_undo++;
    this->stack.push_back(make_unique<AddAction>(s, this->repo));
}

void Service::removeSongFromRepository(const std::string & artist, const std::string & title)
{
	Song s = this->repo.findByArtistAndTitle(artist, title);
	this->repo.removeSong(s);
    if(this->stack.size() != this->current_undo) {
        this->stack.erase(this->stack.begin()+this->current_undo, this->stack.end());
    }
    this->current_undo++;
    this->stack.push_back(make_unique<RemoveAction>(s, this->repo));
}

void Service::addSongToPlaylist(const Song& song)
{
	if (this->playList == nullptr)
		return;
	this->playList->add(song);
}

void Service::addAllSongsByArtistToPlaylist(const std::string& artist)
{
	vector<Song> songs = this->repo.getSongs();
	int nSongs = static_cast<int>(count_if(songs.begin(), songs.end(),
		[artist](const Song& s)
		{
			return s.getArtist() == artist;
		}));

	vector<Song> songsByArtist(nSongs);
	copy_if(songs.begin(), songs.end(), songsByArtist.begin(),
		[artist](const Song& s)
		{
			return s.getArtist() == artist;
		});

	for (auto s : songsByArtist)
		this->playList->add(s);
}

void Service::startPlaylist()
{
	if (this->playList == nullptr)
		return;
	this->playList->play();
}

void Service::nextSongPlaylist()
{
	if (this->playList == nullptr)
		return;
	this->playList->next();
}

void Service::savePlaylist(const std::string& filename)
{
	if (this->playList == nullptr)
		return;

	this->playList->setFilename(filename);
	this->playList->writeToFile();
}

void Service::openPlaylist() const
{
	if (this->playList == nullptr)
		return;

	this->playList->displayPlaylist();
}

void Service::undo() {
    if(this->stack.empty() || this->current_undo == 0) {
        throw exception();
        return;
    }

    this->stack[this->current_undo-1]->executeUndo();
    this->current_undo--;

}

void Service::redo() {
    if(this->stack.empty() || this->stack.size() == this->current_undo) {
        throw exception();
        return;
    }

    this->stack[this->current_undo]->executeRedo();
    this->current_undo++;
}

void Service::updateSongFromRepository(const string &artist, const string &title, double minutes, double seconds,
                                       const string &source, const string &artist2, const string &title2) {

    Song s{ artist, title, Duration{minutes, seconds}, source };
    this->validator.validate(s);
    Song s2{artist2, title2, Duration{minutes, seconds}, source};
    this->validator.validate(s2);
    this->repo.updateSong(s, s2);




}
