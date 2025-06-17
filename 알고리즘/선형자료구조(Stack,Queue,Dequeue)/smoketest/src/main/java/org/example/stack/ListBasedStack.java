package org.example.stack;

import org.example.stack.AdtStack;

import java.util.Arrays;

public class ListBasedStack<T> implements AdtStack<T> {
    private int top;
    private T[] array_list;

    @SuppressWarnings("unchecked")
    public ListBasedStack() {
        this.top = -1;
        this.array_list = (T[]) new Object[1];
    }

    @SuppressWarnings("unchecked")
    private void resize(int newCapacity) {
        T[] newArray = (T[]) new Object[newCapacity];
        System.arraycopy(this.array_list, 0, newArray, 0, Math.min(array_list.length, newCapacity));
        this.array_list = newArray;
    }

    @Override
    public void push(T item) {
        if (top + 1 == array_list.length) {
            resize(2 * array_list.length);
        }
        this.top++;
        array_list[top] = item;
    }

    @Override
    public T pop() {
        if (top == -1) {
            throw new RuntimeException("Stack is empty");
        }
        T item = array_list[top];
//        array_list[top] = null;
        top--;
//        if (top >= 1 && top < array_list.length / 4) {
//            resize(array_list.length / 2);
//        }
        return item;
    }

    @Override
    public T peek() {
        if (top == -1) {
            throw new RuntimeException("Stack is empty");
        }
        return array_list[top];
    }

    @Override
    public boolean empty() {
        if (top == -1){
//            System.out.println("true");
            return true;
        }
//        System.out.println("false");
        return false;
    }

    @Override
    public int size() {
        return top + 1;
    }
}