public class Main {
    public static void main(String[] args) {
//        <Linked List>
//        LinkedList ll = new LinkedList();
//        ll.append(2);
//        ll.preAppend(1);
//        ll.display();
//        System.out.println(ll.getSize());

//        <Stack>
//        Stack stack = new Stack();
//        stack.isEmpty();
//        stack.push(1);
//        stack.push(2);
//        stack.push(3);
//        stack.push(4);
//        stack.push(5);
//        stack.pop();
//        stack.push(6);
//        stack.getSize();
//        stack.isEmpty();

//        <Queue>
        Queue queue = new Queue();
        queue.pop();
        queue.front();
        queue.back();
        queue.isEmpty();
        queue.getSize();
        queue.push(3);
        System.out.println("---");
        queue.push(5);
        System.out.println("---");
        queue.pop();
        System.out.println("---");
        queue.push(10);
        System.out.println("---");
        queue.push(7);
        System.out.println("---");
        queue.pop();
        System.out.println("---");
        queue.pop();
        System.out.println("---");
        queue.push(11);
        System.out.println("---");
        queue.push(2);
        System.out.println("---");
        queue.pop();
        System.out.println("---");
        queue.pop();
        System.out.println("---");
        queue.push(9);
        System.out.println("---");
        queue.push(6);
        System.out.println("---");
        queue.front();
        queue.back();
        queue.isEmpty();
        queue.getSize();
    }
}