package repository;

/* 1.2. Repository: is an in-memory repository.
Please use fixed size array to implement the
collection of the problem entities.
*/

import model.Vegetable;

public class Repository implements Repo {

    private Vegetable[] repo = new Vegetable[100];
    private int size;
    private int fill;

    @Override
    public int getSize() {
        return this.size;
    }

    @Override
    public int getFill() {
        return this.fill;
    }

    public Repository() {
        this.size = 100;
        this.fill = 0;
    }

    @Override
    public void addToRepo(Vegetable v) {
        if (this.getFill() == this.getSize()) { // if the array is full
            Vegetable[] new_arr = new Vegetable[this.getSize() * 2];
            this.size *= 2;
            if (this.fill >= 0) System.arraycopy(this.repo, 0, new_arr, 0, this.fill); // replacing new array
            this.repo = new_arr; // replacing
        }
        this.repo[this.fill] = v;
        this.fill++;
    }

    public void removeFromRepo(int index) throws RepoException {
        if (index >= this.fill) { // trying to remove bad element
            throw new RepoException("Can't remove nonexistent element!");
        } else if (index == this.fill - 1) { // removing last element
            this.repo[index] = null;
            this.fill--;
        } else {
            for (int i = index; i < this.fill - 1; i++) {
                this.repo[i] = this.repo[i + 1];
            }
            this.fill--;
        }
    }

    @Override
    public Vegetable getElement(int index){
        return this.repo[index];
    }
}
