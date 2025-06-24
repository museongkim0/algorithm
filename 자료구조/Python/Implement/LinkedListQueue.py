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
        if self.list.search(0) == None:
            return None
        return self.list.search(0)

    def back(self) -> Optional[T]:
        if self.list.search(self.list.size - 1) == None:
            return None
        return self.list.search(self.list.size - 1)

    def get_size(self) -> int:
        return self.list.size

    def is_empty(self) -> bool:
        return self.list.size == 0

    def display(self):
        return self.list.display()

# queue = LinkedListQueue()
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
