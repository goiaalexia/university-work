package Model.DataStructures;

import java.util.Deque;

import Model.Exceptions.StackException;

public interface IStack<T> extends Iterable<T> {
    T pop() throws StackException;

    T peek() throws StackException;

    void push(T v);

    boolean isEmpty();

    Deque<T> getStack();
}
