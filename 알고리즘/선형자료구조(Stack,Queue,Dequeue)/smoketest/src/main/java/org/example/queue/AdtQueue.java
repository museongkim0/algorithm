package org.example.queue;

public interface AdtQueue<T>{
    void push(T item);
    T pop();
    T front();
    T back();
    boolean empty();
    int size();
}
