from typing import TypeVar, Optional

from ADT.ADTLinkedList import ADTLinkedList
# T에 대한 부분 질문하기
T = TypeVar('T')

class DoubleLinkedList(ADTLinkedList[T]):
    class Node:
        def __init__(self, data: T):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # TODO : size 증가 코드 중복 없게 앞 또는 뒤에 추가
    def append(self, data: T) -> None:
        new_node = self.Node(data)
        self.size += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data: T) -> None:
        new_node = self.Node(data)
        self.size += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def search(self, index: int) -> Optional[T]:
        if not self.head:
            return None
        elif index > self.size - 1:
            return None
        count = 0
        current = self.head
        while count != index:
            count += 1
            current = current.next
        return current.data

    def __search_node(self, index: int):
        if not self.head:
            return None
        elif index > self.size-1:
            return None
        count = 0
        current = self.head
        while count != index:
            count += 1
            current = current.next
        return current

    def search_last(self) -> Optional[T]:
        if not self.head:
            return None
        return self.tail.data

    # TODO: if문으로 조기 리턴이 되는 것은 else가 필요하지 않음 / index out of range 수정
    def insert(self, index: int, data: T) -> None:
        new_node = self.Node(data)
        self.size += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            count = 0
            current = self.head
            while current:
                if count == index:
                    new_node.next = current
                    new_node.prev = current.prev
                    if index != 0:
                        current.prev.next = new_node
                    else:
                        self.head = new_node
                    current.prev = new_node
                    return
                count += 1
                current = current.next
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def replace(self, index: int, data: T) -> None:
        search_node = self.__search_node(index)
        if search_node == None:
            return None
        search_node.data = data

    def erase(self, index: int) -> Optional[T]:
        if index > self.size - 1:
            return None
        search_node = self.__search_node(index)
        self.size -= 1
        if index == 0:
            if self.head == self.tail:
                current = self.head
                self.head = None
                self.tail = None
                return current.data
            current = self.head
            self.head = self.head.next
            self.head.prev = None
            return current.data
        prev_node = search_node.prev
        prev_node.next = search_node.next
        if search_node.next == None:
            self.tail = prev_node
        else:
            search_node.next.prev = prev_node

        return search_node.data

    def erase_last(self) -> Optional[T]:
        if not self.head:
            return None
        self.size -= 1
        if self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            return current.data
        node = self.tail
        node.prev.next = None
        self.tail = node.prev
        return node.data

    def get_size(self) -> int:
        return self.size

    def display(self):
        if not self.head:
            return
        current = self.head
        answer = []
        while current:
            answer.append(current.data)
            current = current.next
        return answer

# ll = DoubleLinkedList()
# ll.append(1)
# ll.append(2)
# ll.prepend(3)
# print(ll.display())
# print(ll.search(2))
# print(ll.search(4))
# ll.insert(1, 4)
# print(ll.display())
# ll.insert(5, 7)
# print(ll.display())
# ll.replace(1, 6)
# print(ll.display())
# print(ll.search(3))
# print(ll.erase(3))
# print(ll.display())
# print(ll.get_size())
# print(ll.erase(3))