from ADT.ADTDeque import ADTDeque
from Implement.DoubleLinkedList import DoubleLinkedList
from typing import TypeVar, Optional

T = TypeVar('T')

class LinkedListDeque(ADTDeque[T]):
    def __init__(self):
        self.list = DoubleLinkedList()

    def append(self, item: T) -> None:
        self.list.append(item)

    def appendleft(self, item: T) -> None:
        self.list.prepend(item)

    def pop(self) -> Optional[T]:
        return self.list.erase_last()

    def popleft(self) -> Optional[T]:
        return self.list.erase(0)

    def peek_front(self) -> Optional[T]:
        return self.list.search(0)

    def peek_back(self) -> Optional[T]:
        return self.list.search_last()

    def is_empty(self) -> bool:
        if self.list.size == 0:
            return True
        else:
            return False

    def get_size(self) -> int:
        return self.list.size

    def display(self):
        return self.list.display()


# deque = LinkedListDeque()
# print(deque.popleft())
# print(deque.is_empty())
# print(deque.get_size())
# deque.append(1)
# deque.appendleft(3)
# deque.append(5)
# deque.appendleft(7)
# print(deque.display())
# print(deque.pop())
# print(deque.display())
# print(deque.popleft())
# print(deque.display())
# print(deque.peek_front())
# print(deque.peek_back())
# print(deque.popleft())
# print(deque.is_empty())
# print(deque.get_size())