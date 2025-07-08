package org.example.Queue;

import java.util.Arrays;
import java.util.Optional;

//TODO: size 변수 없애고, front/back 이용하여 size 함수 만들기
public class ArrayQueue<T> implements AdtQueue<T> {
    private int front;
    private int back;
    private int size;
    private Object[] arr;

    private static final int DEFAULT_CAPACITY = 10;
    private static final int RESIZE_FACTOR = 2;

    public ArrayQueue(){
        this.front = 0;
        this.back = 0;
        this.size = 0;
        this.arr = new Object[DEFAULT_CAPACITY];
    }

    public ArrayQueue(int capacity){
        if (capacity <= 0){
            throw new IllegalArgumentException("Initial capacity must be positive.");
        }
        this.front = 0;
        this.back = 0;
        this.size = 0;
        this.arr = new Object[capacity];
    }

    private void resize(int newCapacity){
        Object[] newArray = new Object[newCapacity];
        for(int i = 0; i < size; i++){
            newArray[i] = arr[front];
            front = (front + 1) % size;
        }
        this.arr = newArray;
        this.front = 0;
        this.back = size;
        System.out.println("배열 크기 확장됨: " + arr.length+" front: "+front+" back: "+back);
    }

    @Override
    public void push(T data){
        if (size == arr.length){
            resize(RESIZE_FACTOR*arr.length);
        }
        arr[back] = data;
        back = (back + 1) % arr.length;
        size ++;
    }

    @Override
    public Optional<T> pop(){
        if (size == 0){
            return Optional.empty();
        }
        @SuppressWarnings("unchecked")
        T var = (T) arr[front];
        front = (front + 1) % arr.length;
        size --;
        return Optional.of(var);
    }

    @Override
    public Optional<T> front(){
        if (size == 0){
            return Optional.empty();
        }
        @SuppressWarnings("unchecked")
        T var = (T) arr[front];
        return Optional.of(var);
    }

    @Override
    public Optional<T> back(){
        if (size == 0){
            return Optional.empty();
        }
        int index = (back-1)&size;
        @SuppressWarnings("unchecked")
        T var = (T) arr[index];
        return Optional.of(var);
    }

    @Override
    public boolean isEmpty(){
        return this.size == 0;
    }


    @Override
    public int getSize(){
        return this.size;

    }

    public void display(){
        System.out.println(Arrays.toString(this.arr));
    }
}
