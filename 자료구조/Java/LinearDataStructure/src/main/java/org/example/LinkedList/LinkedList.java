package org.example.LinkedList;


public class LinkedList<T> {
    private Node<T> head;
    private int size;

    public LinkedList(){
        this.head = null;
        this.size = 0;
    }

    public void append(T data) {
        Node<T> newNode = new Node<T>(data);
        if (head == null){
            this.head = newNode;
            this.size += 1;
        }
        else {
            Node<T> current = this.head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
            this.size += 1;
        }
    }

    public void preAppend(T data) {
        Node<T> newNode = new Node<T>(data);
        if (head == null){
            this.head = newNode;
            this.size += 1;
        }
        else {
            newNode.next = this.head;
            this.head = newNode;
            this.size += 1;
        }
    }

    public Node<T> find(T data) {
        if (head == null){
            return null;
        }
        else {
            Node<T> current = this.head;
            while (current != null) {
                if (current.data == data){
                    return current;
                } else {
                    current = current.next;
                }
            }
            return null;
        }
    }

    public Node<T> findFirst() {
        if (head == null){
            return null;
        }
        else {
            return this.head;
        }
    }

    public void display() {
        if (head != null){
            Node<T> current = this.head;
            while (current != null){
                System.out.println(current.data);
                current = current.next;
            }
        }
    }

    public int getSize(){
        return this.size;
    }
}
