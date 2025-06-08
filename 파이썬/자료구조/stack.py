from linked_list import LinkedList

class stackLinked:
    def __init__(self):
        self.list = LinkedList()
    
    def push(self, data):
        self.list.preAppend(data)
        return self.list
        
    def pop(self):
        findNode = self.list.findFirst()
        if not findNode:
            print("no value")
            return None
        else:
            self.list.erase(findNode)
        return findNode.data
    
    def top(self):
        if not self.list.findFirst():
            print("no value")
            return None
        else:
            print(self.list.findFirst().data)
            return self.list.findFirst().data
    
    def size(self):
        print(self.list.size)
    
    def isEmpty(self):
        if self.list.size == 0:
            print("True")
        else:
            print("False")
    
    def display(self):
        self.list.display()

linked_stack = stackLinked()
linked_stack.top()
linked_stack.pop()
linked_stack.isEmpty()
linked_stack.push(3)
linked_stack.display()
linked_stack.push(5)
linked_stack.display()
linked_stack.push(7)
linked_stack.display()
print(linked_stack.pop())
linked_stack.display()
linked_stack.top()
linked_stack.isEmpty()
linked_stack.size()