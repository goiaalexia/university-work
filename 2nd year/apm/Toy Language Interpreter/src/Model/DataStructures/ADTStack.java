package Model.DataStructures;

import java.util.Deque;
import java.util.Iterator;
import java.util.LinkedList;

import Model.Exceptions.StackException;

public class ADTStack<T> implements IStack<T> {
    private final Deque<T> deque;

    public ADTStack(ADTStack c){
        this.deque = new LinkedList<>(c.deque);
    }

    public ADTStack() {
        deque = new LinkedList<>();
    }

    @Override
    public T pop() throws StackException {
        if (deque.isEmpty()) {
            throw new StackException("Stack is empty!");
        }
        return deque.pop();
    }

    @Override
    public T peek() throws StackException {
        if (deque.isEmpty()) {
            throw new StackException("Stack is empty!");
        }
        return deque.peek();
    }

    @Override
    public void push(T v) {
        deque.push(v);
    }

    @Override
    public boolean isEmpty() {
        return deque.isEmpty();
    }

    @Override
    public Iterator<T> iterator() {
        return deque.iterator();
    }

    @Override
    public Deque<T> getStack() {
        return deque;
    }
}
