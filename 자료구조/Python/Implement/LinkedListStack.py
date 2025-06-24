from ADT.ADTStack import ADTStack
from Implement.LinkedList import LinkedList
from typing import TypeVar, Optional

T = TypeVar('T')

# TODO: 파스칼 케이스로 변경 StackLinked
class LinkedListStack(ADTStack[T]):
    def __init__(self):
        self.list = LinkedList()

    def push(self, item: T) -> None:
        self.list.prepend(item)

    # TODO: foundNode
    def pop(self) -> Optional[T]:
        return self.list.erase(0)

    def top(self) -> Optional[T]:
        if self.list.search(0) == None:
            return None
        return self.list.search(0)

    def get_size(self) -> int:
        return self.list.size

    # TODO: return으로 변경
    def is_empty(self) -> bool:
        if self.list.size == 0:
            return True
        else:
            return False

    def display(self):
        return self.list.display()

# linked_stack = LinkedListStack()
# print(linked_stack.top())
# print(linked_stack.pop())
# print(linked_stack.isEmpty())
# linked_stack.push(3)
# print(linked_stack.display())
# linked_stack.push(5)
# print(linked_stack.display())
# linked_stack.push(7)
# print(linked_stack.display())
# print(linked_stack.pop())
# print(linked_stack.display())
# print(linked_stack.top())
# print(linked_stack.isEmpty())
# print(linked_stack.getSize())
