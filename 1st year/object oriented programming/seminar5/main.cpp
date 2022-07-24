#include "UI.h"
#include "CSVPlayList.h"
#include "RepositoryExceptions.h"

using namespace std;

int main()
{
	try
	{
		Repository repo(R"(C:\Users\lexig\CLionProjects\seminar5\songs)");
		FilePlaylist* p = new CSVPlaylist{};
		Service serv(repo, p, SongValidator{});
		UI ui(serv);
		ui.run();
		delete p;
	}
	catch (FileException&)
	{
		cout << "Repository file could not be opened! The application will terminate." << endl;
		return 1;
	}

	return 0;
}