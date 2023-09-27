package controller;

/*
1.3. Controller: implements the functionality required by the problem
and the operations to add and remove entities from the repository.
It maintains a reference to the repository. The reference type is an interface
such that we can easily replace the repository implementation.
*/

import model.Vegetable;
import repository.RepoException;
import repository.Repository;
import repository.Repo;

public class Service {

    private Repo repo;

    public Service() {
        this.repo = new Repository();
    }

    public Service(Repo r){
        this.repo = r;
    }

    public Repo getElements(){
        return this.repo;
    }

    public void addVegetable(Vegetable v) {
        this.repo.addToRepo(v);
    }
    // I treated the situation where the repo is full by manually resizing it, although
    // I could've thrown an exception

    public void removeVegetable(int index) throws RepoException {
        this.repo.removeFromRepo(index);
    }
    // throws exception when index is out of bounds

    public Repo weightedVegetables(){
        Repo sol = new Repository();
        for (int i = 0; i < this.repo.getFill(); i++) {
            if(this.repo.getElement(i).getWeight()>0.2){
                sol.addToRepo(this.repo.getElement(i));
            }
        }
        return sol;
    } // throws exception when the index of getElement is out of bounds


}
