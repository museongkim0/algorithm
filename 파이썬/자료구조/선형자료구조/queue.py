class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
    
    def findFirst(self):
        if not self.head:
            return None
        else:
            return self.head.data
    
    def findLast(self):
        if not self.head:
            return None
        else:
            return self.tail.data
            
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

class Queue:
    def __init__(self):
        self.list = LinkedList()
            
    def push(self, data):
        self.list.append(data)
        self.list.display()
    
    def pop(self):
        answer = self.list.eraseFirst()
        if not answer:
            print("Queue is empty")
        else:
            print(answer)
            self.list.display()
            return answer
    
    def front(self):
        answer = self.list.findFirst()
        if not answer:
            print("Queue is empty")
        else:
            print(answer)
            return answer
    
    def back(self):
        answer = self.list.findLast()
        if not answer:
            print("Queue is empty")
        else:
            print(answer)
            return answer
        
    def isEmpty(self):
        if self.list.size == 0:
            print("True")
            return True
        else:
            print("False")
            return False
    
    def getSize(self):
        print(self.list.size)
        return self.list.size
    
queue = Queue()
queue.pop()
queue.front()
queue.back()
queue.isEmpty()
queue.getSize()
queue.push(3)
queue.push(5)
queue.pop()
queue.push(10)
queue.push(7)
queue.front()
queue.back()
queue.isEmpty()
queue.getSize()