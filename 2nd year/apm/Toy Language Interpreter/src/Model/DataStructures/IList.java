package Model.DataStructures;

import java.util.List;
import java.util.function.Consumer;

import Model.Exceptions.ListException;

public interface IList<T> extends Iterable<T> {
    T pop() throws ListException;

    void add(T v);

    @Override
    void forEach(Consumer<? super T> action);

    boolean isEmpty();

    java.util.List<T> getList();
}
