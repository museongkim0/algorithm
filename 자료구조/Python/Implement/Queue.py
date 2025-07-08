from ADT.ADTQueue import ADTQueue
from Implement.LinkedList import LinkedList
from typing import TypeVar, Optional

T = TypeVar('T')

class LinkedListQueue(ADTQueue[T]):
    def __init__(self):
        self.list = LinkedList()

    def push(self, item: T) -> None:
        self.list.append(item)

    def pop(self) -> Optional[T]:
        return self.list.erase(0)

    def front(self) -> Optional[T]:
        if self.list.search(0) is None:
            return None
        return self.list.search(0)

    def back(self) -> Optional[T]:
        if self.list.search(self.list.size - 1) is None:
            return None
        return self.list.search(self.list.size - 1)

    def get_size(self) -> int:
        return self.list.size

    def is_empty(self) -> bool:
        return self.list.size == 0

    def display(self):
        return self.list.display()


from Implement.Stack import LinkedListStack

# TODO: 리스트가 비었을 때 옮기는 부분 추상화 하기
class TwoStackQueue(ADTQueue[T]):
    def __init__(self):
        self.list1 = LinkedListStack()
        self.list2 = LinkedListStack()

    def push(self, item: T) -> None:
        self.list1.push(item)

    def __move(self, list0):
        if list0 == self.list1:
            while not self.list1.is_empty():
                self.list2.push(self.list1.pop())
        if list0 == self.list2:
            while not self.list2.is_empty():
                self.list1.push(self.list2.pop())

    def pop(self) -> Optional[T]:
        if self.list2.is_empty():
            self.__move(self.list1)
        return self.list2.pop()

    def front(self) -> Optional[T]:
        if self.list2.is_empty():
            self.__move(self.list1)
        return self.list2.top()

    def back(self) -> Optional[T]:
        if self.list1.is_empty():
            self.__move(self.list2)
        return self.list1.top()

    def get_size(self) -> int:
        return self.list1.get_size() + self.list2.get_size()

    def is_empty(self) -> bool:
        return self.list1.is_empty() and self.list2.is_empty()

    def display(self):
        if self.list1.is_empty():
            return self.list2.display()
        elif self.list2.is_empty():
            return self.list1.display()[::-1]
        return self.list2.display() + self.list1.display()[::-1]


# queue = LinkedListQueue()
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
