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
            if self.head == None:
                self.tail = self.head
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
    
    def pop(self):
        answer = self.list.eraseFirst()
        if not answer:
            # print("-1")
            return '-1'
        else:
            # print(answer)
            return answer
    
    def front(self):
        answer = self.list.findFirst()
        if not answer:
            # print("-1")
            return '-1'
        else:
            # print(answer)
            return answer
    
    def back(self):
        answer = self.list.findLast()
        if not answer:
            # print("-1")
            return '-1'
        else:
            # print(answer)
            return answer
        
    def isEmpty(self):
        if self.list.size == 0:
            # print("1")
            return '1'
        else:
            # print("0")
            return '0'
    
    def getSize(self):
        # print(self.list.size)
        return self.list.size

import sys

queue = Queue()

for i in range(int(sys.stdin.readline().rstrip())):
   queue.push(i+1)

while queue.getSize() != 1:
    queue.pop()
    queue.push(queue.pop())

print(queue.front())