public class LinkedList {
    private Node head;
    private int size;

    public LinkedList(){
        this.head = null;
        this.size = 0;
    }

    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null){
            this.head = newNode;
            this.size += 1;
        }
        else {
            Node current = this.head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
            this.size += 1;
        }
    }

    public void preAppend(int data) {
        Node newNode = new Node(data);
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

    public Node find(int data) {
        if (head == null){
            return null;
        }
        else {
            Node current = this.head;
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

    public Node findFirst() {
        if (head == null){
            return null;
        }
        else {
            return this.head;
        }
    }

    public void display() {
        if (head != null){
            Node current = this.head;
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
