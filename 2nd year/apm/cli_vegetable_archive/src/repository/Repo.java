package repository;

import model.Vegetable;

public interface Repo {
    int getSize();
    int getFill();

    void addToRepo(Vegetable v);
    void removeFromRepo(int index) throws RepoException;

    Vegetable getElement(int index);

}
