class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def preAppend(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.size += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.size += 1
    
    def findFirst(self):
        if not self.head:
            return None
        else:
            return self.head.data
            
    def eraseFirst(self):
        if not self.head:
            return None
        else:
            current = self.head
            self.head = current.next
            self.size -= 1
            return current.data
        
    def display(self):
        if not self.head:
            return
        else:
            current = self.head
            answer = []
            while current:
                answer.append(current.data)
                current = current.next
            print(answer, self.size)

class Stack:
    def __init__(self):
        self.list = LinkedList()
    
    def push(self, data):
        self.list.preAppend(data)
        return self.list
        
    def pop(self):
        pop_var = self.list.eraseFirst()
        if not pop_var:
            print("NO")
            return None
        # else:
        #     print(pop_var)
        return pop_var
    
    def top(self):
        top_var = self.list.findFirst()
        if not top_var:
            print("-1")
            return None
        else:
            print(top_var)
            return top_var
    
    def size(self):
        # print(self.list.size)
        return self.list.size
    
    def isEmpty(self):
        if self.list.size == 0:
            print("1")
        else:
            print("0")
    
    def display(self):
        self.list.display()
        
import sys
stack = Stack()

for _ in range(int(sys.stdin.readline().strip())):
    answer = sys.stdin.readline().strip()
    stack = Stack()
    check_var = False
    for i in answer:
        if i == "(":
            stack.push(1)
        else:
            pop_var = stack.pop()
            if pop_var == None:
                check_var = True
                break
    if check_var:
        continue
    if stack.size() == 0:
        print("YES")
    else:
        print("NO")    