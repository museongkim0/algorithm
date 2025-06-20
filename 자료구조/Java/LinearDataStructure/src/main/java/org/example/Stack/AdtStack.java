package org.example.Stack;

import java.util.Optional;

public interface AdtStack<T> {
    void push(T item);

    Optional<T> pop();

    Optional<T> top();

    int getSize();

    boolean isEmpty();
}
