from ADT.ADTQueue import ADTQueue, T
from Implement.LinkedList import LinkedList
from typing import Optional

class LinkedListQueue(ADTQueue[T]):
    def __init__(self):
        self.list = LinkedList()

    def push(self, item: T) -> None:
        self.list.append(item)

    def pop(self) -> Optional[T]:
        return self.list.erase(0)

    def front(self) -> Optional[T]:
        if not self.list.search(0):
            return None
        return self.list.search(0).data

    def back(self) -> Optional[T]:
        if not self.list.search(self.list.size - 1):
            return None
        return self.list.search(self.list.size - 1).data

    def get_size(self) -> int:
        return self.list.size

    def is_empty(self) -> bool:
        if self.list.size == 0:
            return True
        else:
            return False

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
