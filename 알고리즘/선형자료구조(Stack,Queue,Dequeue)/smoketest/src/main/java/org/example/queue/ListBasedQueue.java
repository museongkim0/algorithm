package org.example.queue;

public class ListBasedQueue<T> implements AdtQueue<T> {
    private int front;
    private int back;
    private int size;
    private T[] arr;

    @SuppressWarnings("unchecked")
    public ListBasedQueue() {
        this.front = 0;
        this.back = 0;
        this.size = 0;
        this.arr = (T[]) new Object[1];
    }

    @SuppressWarnings("unchecked")
    private void resize(int newCapacity) {
        T[] newArray = (T[]) new Object[newCapacity];
        for(int i = 0; i < size; i++){
            newArray[i] = arr[front];
            front = (front + 1) % size;
        }
        this.arr = newArray;
        this.front = 0;
        this.back = size;
    }

    @Override
    public void push(T item) {
        if (size == arr.length){
            resize(2*arr.length);
        }
        arr[back] = item;
        back = (back + 1) % arr.length;
        size ++;
    }

    @Override
    public T pop() {
        if (size == 0){
            throw new RuntimeException("Queue is empty");
        }
        else {
            T item = arr[front];
            front = (front + 1) % arr.length;
            size --;
            return item;
        }
    }

    @Override
    public T front() {
        if (size == 0){
            throw new RuntimeException("Queue is empty");
        }
        else {
            return arr[front];
        }
    }

    @Override
    public T back() {
        if (size == 0){
            throw new RuntimeException("Queue is empty");
        }
        else {
            return arr[back];
        }
    }

    @Override
    public boolean empty() {
        if (size == 0){
//            System.out.println("True");
            return true;
        }
        else {
//            System.out.println("False");
            return false;
        }
    }

    @Override
    public int size() {
        return size;
    }
}
