public class Stack {
    private int top;
    private int[] array_list;

    public Stack(){
        this.top = -1;
        this.array_list = new int[1];
    }

    private void resize(int newCapacity) {
        int[] newArray = new int[newCapacity];
        System.arraycopy(this.array_list, 0, newArray, 0, array_list.length);
        // 또는 Arrays.copyOf 사용:
        // int[] newArray = Arrays.copyOf(array_list, newCapacity);

        this.array_list = newArray; // 스택의 배열을 새로 만든 배열로 교체
        System.out.println("배열 크기 확장됨: " + array_list.length); // 디버깅용
    }

    public void push(int data){
        if (top + 1 == array_list.length) {
            resize(2 * array_list.length);
        }
        this.top++;
        array_list[top] = data;
    }

    public int pop(){
        if (top == -1){
            return -1;
        }
        int var = array_list[top];
        System.out.println("pop: "+var);
        top --;
        return var;
    }

    public int top(){
        if (top == -1){
            return -1;
        }
        return array_list[top];
    }

    public int getSize(){
        System.out.println(top+1);
        return top+1;
    }

    public boolean isEmpty(){
        if (top == -1){
            System.out.println("true");
            return true;
        }
        System.out.println("false");
        return false;
    }
}
