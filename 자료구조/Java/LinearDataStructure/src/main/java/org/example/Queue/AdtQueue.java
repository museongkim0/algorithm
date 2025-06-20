package org.example.Queue;

import java.util.Optional;

public interface AdtQueue<T>{
    void push(T item);

    Optional<T> pop();

    Optional<T> front();

    Optional<T> back();

    int getSize();

    boolean isEmpty();
}
