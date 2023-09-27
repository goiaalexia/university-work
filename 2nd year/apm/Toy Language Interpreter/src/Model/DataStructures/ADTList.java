package Model.DataStructures;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.function.Consumer;

import Model.Exceptions.ListException;

public class ADTList<T> implements IList<T> {
    public java.util.List<T> list;

    public ADTList() {
        list = new LinkedList<>();
    }

    public ADTList(java.util.List<T> l) {
        list = l;
    }

    @Override
    public T pop() throws ListException {

        if (list.size() > 0) {
            T newList = list.get(0);
            list.remove(0);
            return newList;
        }

        throw new ListException("Cannot pop because the list is empty!");
    }

    @Override
    public void add(T v) {
        list.add(v);
    }

    @Override
    public void forEach(Consumer<? super T> action) {
        list.forEach(action);
    }

    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public Iterator<T> iterator() {
        return list.iterator();
    }

    @Override
    public java.util.List<T> getList() {
        return list;
    }
}
