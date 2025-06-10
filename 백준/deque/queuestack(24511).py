class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoubleLinkedList:
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
            newNode.prev = self.tail
            self.tail = newNode
            self.size += 1
    
    def preAppend(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
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
            else:
                self.head.prev = None
            self.size -= 1
            return current.data
    
    def eraseLast(self):
        if not self.head:
            return None
        else:
            current = self.tail
            self.tail = current.prev
            if self.tail == None:
                self.head = self.tail
            else:
                self.tail.next = None
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
            
class Deque:
    def __init__(self):
        self.list = DoubleLinkedList()

    def push_front(self, data):
        self.list.preAppend(data)
            
    def push_back(self, data):
        self.list.append(data)
    
    def pop_front(self):
        answer = self.list.eraseFirst()
        if not answer:
            return '-1'
        else:
            return answer
        
    def pop_back(self):
        answer = self.list.eraseLast()
        if not answer:
            return '-1'
        else:
            return answer
    
    def front(self):
        answer = self.list.findFirst()
        if not answer:
            return '-1'
        else:
            return answer
    
    def back(self):
        answer = self.list.findLast()
        if not answer:
            return '-1'
        else:
            return answer
        
    def isEmpty(self):
        if self.list.size == 0:
            return '1'
        else:
            return '0'
    
    def getSize(self):
        return str(self.list.size)
    
    def display(self):
        self.list.display()

import sys

deque = Deque()

N = int(sys.stdin.readline().rstrip())

A = sys.stdin.readline().rstrip().split()

B = sys.stdin.readline().rstrip().split()

M = int(sys.stdin.readline().rstrip())

C = sys.stdin.readline().rstrip().split()


for i in range(N):
    if A[i] == '0':
        deque.push_back(B[i])

answer_list = []
for j in range(M):
    deque.push_front(C[j])
    answer_list.append(deque.pop_back())

print(' '.join(answer_list))
