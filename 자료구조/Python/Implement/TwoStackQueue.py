from ADT.ADTQueue import ADTQueue, T
from Implement.LinkedListStack import LinkedListStack
from typing import Optional

class TwoStackQueue(ADTQueue[T]):
    def __init__(self):
        self.list1 = LinkedListStack()
        self.list2 = LinkedListStack()

    def push(self, item: T) -> None:
        self.list1.push(item)

    def pop(self) -> Optional[T]:
        if self.list2.is_empty():
            while not self.list1.is_empty():
                self.list2.push(self.list1.pop())
        return self.list2.pop()

    def front(self) -> Optional[T]:
        if self.list2.is_empty():
            while not self.list1.is_empty():
                self.list2.push(self.list1.pop())
        return self.list2.top()

    def back(self) -> Optional[T]:
        if self.list1.is_empty():
            while not self.list2.is_empty():
                self.list1.push(self.list2.pop())
        return self.list1.top()

    def get_size(self) -> int:
        return self.list1.get_size() + self.list2.get_size()

    def is_empty(self) -> bool:
        if self.list1.is_empty() & self.list2.is_empty():
            return True
        else:
            return False

    def display(self):
        if self.list1.is_empty():
            return self.list2.display()
        elif self.list2.is_empty():
            return self.list1.display()[::-1]
        return self.list2.display() + self.list1.display()[::-1]

# queue = TwoStackQueue()
# print(queue.pop())
# print(queue.front())
# print(queue.back())
# print(queue.is_empty())
# print(queue.get_size())
# queue.push(3)
# queue.push(5)
# print(queue.display())
# print(queue.pop())
# print(queue.display())
# queue.push(10)
# queue.push(7)
# print(queue.display())
# print(queue.front())
# print(queue.back())
# print(queue.is_empty())
# print(queue.get_size())