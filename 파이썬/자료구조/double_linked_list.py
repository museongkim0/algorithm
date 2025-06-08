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
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current
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
    
    def find(self, data):
        if not self.head:
            return None
        else:
            current = self.head
            while current:
                if current.data == data:
                    return current
                else:
                    current = current.next
            return None
    
    def insert(self, index, data):
        if index == 0:
            newNode = Node(data)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.size += 1
        else:
            if not self.head:
                return
            else:
                newNode = Node(data)
                count = 0
                current = self.head
                while current:
                    if count == index:
                        newNode.next = current
                        newNode.prev = current.prev
                        current.prev.next = newNode
                        current.prev = newNode
                        self.size += 1
                        return
                    else:
                        count += 1
                        current = current.next
        
    
    def insertBefore(self, node, data):
        if not self.head:
            return
        else:
            newNode = Node(data)
            if not node.prev:
                node.prev = newNode
                newNode.next = node
                self.head = newNode
                self.size += 1
            else:
                newNode.prev = node.prev
                node.prev.next = newNode
                newNode.next = node
                node.prev = newNode
                self.size += 1
            
        
    def insertAfter(self, node, data):
        if not self.head:
            return None
        else:
            newNode = Node(data)
            if not node.next:
                node.next = newNode
                newNode.prev = node
                self.tail = newNode
                self.size += 1
            else:
                newNode.next = node.next
                node.next.prev = newNode
                newNode.prev = node
                node.next = newNode
                self.size += 1
    
    def replace(self, node, data):
        if not self.head:
            return None
        else:
            node.data = data
            
    def erase(self, node):
        if not self.head:
            return None
        else:
            if node == self.head:
                self.head = node.next
                self.head.prev = None
                self.size -= 1
                return
            if node == self.tail:
                self.tail = node.prev
                self.tail.next = None
                self.size -= 1
                return
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
            return
        
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

ll = DoubleLinkedList()
ll.append(1)
ll.display()
ll.preAppend(3)
ll.display()
ll.append(2)
ll.display()
finded_node = ll.find(2)
ll.insertBefore(finded_node,5)
finded_node = ll.find(3)
ll.insertBefore(finded_node,10)
ll.display()
finded_node = ll.find(2)
ll.insertAfter(finded_node,7)
ll.display()
ll.insertAfter(finded_node,9)
ll.display()
ll.replace(finded_node,6)
ll.display()
finded_node = ll.find(10)
ll.erase(finded_node)
ll.display()
finded_node = ll.find(5)
ll.erase(finded_node)
ll.display()
ll.insert(0, 5)
ll.display()
ll.insert(3, 10)
ll.display()
ll.insert(6, 15)
ll.display()