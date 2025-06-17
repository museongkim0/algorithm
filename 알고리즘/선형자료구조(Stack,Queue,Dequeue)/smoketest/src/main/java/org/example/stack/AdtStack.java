package org.example.stack;

public interface AdtStack<T> {
    void push(T item);
    T pop();
    T peek();
    boolean empty();
    int size();
}
