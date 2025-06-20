package org.example.Stack;

import java.util.Arrays;
import java.util.Optional;

// 함수의 abstract를 극대화 해야함 -> 제네릭 잘 활용 필요

// TODO: 어레이 사이즈 가변적으로 사용자가 지정할 수 있게 하는 것이 용이함
// TODO: resize 상수도 사전에 const 변수로 지정하면 좋음
public class ArrayStack<T> implements AdtStack<T> {
    private int top;
    private Object[] array_list;

    private static final int DEFAULT_CAPACITY = 10;
    private static final int RESIZE_FACTOR = 2;

    public ArrayStack(){
        this.top = -1;
        this.array_list = new Object[DEFAULT_CAPACITY];
    }

    public ArrayStack(int capacity){
        if (capacity <= 0){
            throw new IllegalArgumentException("Initial capacity must be positive.");
        }
        this.top = -1;
        this.array_list = new Object[capacity];
    }

    // TODO: 메모리 할당 실패의 경우 로직 추가
    private void resize(int newCapacity) {
        Object[] newArray = new Object[newCapacity];
        System.arraycopy(this.array_list, 0, newArray, 0, array_list.length);
        // 또는 Arrays.copyOf 사용:
        // int[] newArray = Arrays.copyOf(array_list, newCapacity);

        this.array_list = newArray; // 스택의 배열을 새로 만든 배열로 교체
        System.out.println("배열 크기 확장됨: " + array_list.length); // 디버깅용
    }

    // TODO: print를 나눠서 할 필요 없음
    @Override
    public void push(T data){
        if (top + 1 == array_list.length) {
            resize(RESIZE_FACTOR * array_list.length);
        }
        this.top++;
        array_list[top] = data;
    }

    // TODO: pop() -> -1이 엘리먼트인지 비어있음을 의미하는건지 알 수 없음 / Optional 사용 고려
    @Override
    public Optional<T> pop(){
        if (top == -1){
            return Optional.empty();
        }
        @SuppressWarnings("unchecked")
        T var = (T) array_list[top];
        top --;
        return Optional.of(var);
    }

    @Override
    public Optional<T> top(){
        if (top == -1){
            return Optional.empty();
        }
        @SuppressWarnings("unchecked")
        T var = (T) array_list[top];
        return Optional.of(var);
    }

    @Override
    public int getSize(){
        return top+1;
    }

    @Override
    public boolean isEmpty(){
        return top == -1;
    }

    public void display(){
        System.out.println(Arrays.toString(this.array_list));
    }
}