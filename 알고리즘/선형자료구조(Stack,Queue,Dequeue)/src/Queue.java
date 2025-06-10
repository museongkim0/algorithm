import java.util.Arrays;

public class Queue {
    private int front;
    private int back;
    private int size;
    private int[] arr;

    public Queue(){
        this.front = 0;
        this.back = 0;
        this.size = 0;
        this.arr = new int[1];
    }

    private void resize(int newCapacity){
        int[] newArray = new int[newCapacity];
        for(int i = 0; i < size; i++){
            newArray[i] = arr[front];
            front = (front + 1) % size;
        }
        this.arr = newArray;
        this.front = 0;
        this.back = size;
        System.out.println("배열 크기 확장됨: " + arr.length);
        System.out.println("front: "+front+" back: "+back);
    }

    public void push(int data){
        if (size == arr.length){
            resize(2*arr.length);
        }
        arr[back] = data;
        back = (back + 1) % arr.length;
        size ++;
        System.out.println(Arrays.toString(arr));
        System.out.println("front: "+front+" back: "+back);
    }

    public int pop(){
        if (size == 0){
            System.out.println("Queue is empty");
            return -1;
        }
        else {
            int pop_var = arr[front];
            front = (front + 1) % arr.length;
            size --;
            System.out.println(Arrays.toString(arr));
            System.out.println("front: "+front+" back: "+back);
            return pop_var;
        }
    }

    public int front(){
        if (size == 0){
            System.out.println("Queue is empty");
            return -1;
        }
        else {
            System.out.println(arr[front]);
            return arr[front];
        }
    }

    public int back(){
        if (size == 0){
            System.out.println("Queue is empty");
            return -1;
        }
        else {
            System.out.println(arr[back-1]);
            return arr[back];
        }
    }

    public boolean isEmpty(){
        if (size == 0){
            System.out.println("True");
            return true;
        }
        else {
            System.out.println("False");
            return false;
        }
    }

    public int getSize(){
        System.out.println(size);
        return size;
    }
}
