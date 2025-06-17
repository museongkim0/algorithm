from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
import random
import unittest
from collections import deque  # 참조 구현으로 사용

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

T = TypeVar('T')

class AbstractDeque(ABC, Generic[T]):
    @abstractmethod
    def append(self, item: T) -> None:
        pass

    @abstractmethod
    def appendleft(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def popleft(self) -> T:
        pass

    @abstractmethod
    def peek_front(self) -> T:
        pass

    @abstractmethod
    def peek_back(self) -> T:
        pass

    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass


class LinkedListDeque(AbstractDeque[T]):
    def __init__(self) -> None:
        # TODO
        self.list = DoubleLinkedList()
        pass

    def append(self, item: T) -> None:
        # TODO
        self.list.append(item)
        pass

    def appendleft(self, item: T) -> None:
        # TODO
        self.list.preAppend(item)
        pass

    def pop(self) -> T:
        # TODO
        answer = self.list.eraseLast()
        if answer is None:
            raise IndexError("Deque is empty")
        else:
            return answer

    def popleft(self) -> T:
        # TODO
        answer = self.list.eraseFirst()
        if answer is None:
            raise IndexError("Deque is empty")
        else:
            return answer

    def peek_front(self) -> T:
        # TODO
        answer = self.list.findFirst()
        if answer is None:
            raise IndexError("Deque is empty")
        else:
            return answer

    def peek_back(self) -> T:
        # TODO
        answer = self.list.findLast()
        if answer is None:
            raise IndexError("Deque is empty")
        else:
            return answer

    def empty(self) -> bool:
        # TODO
        if self.list.size == 0:
            return True
        else:
            return False

    def size(self) -> int:
        # TODO
        return self.list.size


class TestDeque(unittest.TestCase):
    def test_random_operations(self):
        NUM_OPERATIONS = 1000000  # 연산 횟수 (조정 가능)
        REFERENCE_DEQUE = deque()  # collections.deque로 참조 구현
        TEST_DEQUE = LinkedListDeque()  # 테스트 대상 Deque

        OPERATIONS = ["append", "appendleft", "pop", "popleft", "peek_front", "peek_back", "empty", "size"]

        for _ in range(NUM_OPERATIONS):
            op = random.choice(OPERATIONS)

            # Deque가 비었을 때 pop/popleft/peek 방지
            if op in ("pop", "popleft", "peek_front", "peek_back") and len(REFERENCE_DEQUE) == 0:
                continue

            try:
                # 1. append: 오른쪽 끝에 요소 추가
                if op == "append":
                    item = random.randint(-1000, 1000)
                    REFERENCE_DEQUE.append(item)
                    TEST_DEQUE.append(item)

                # 2. appendleft: 왼쪽 끝에 요소 추가
                elif op == "appendleft":
                    item = random.randint(-1000, 1000)
                    REFERENCE_DEQUE.appendleft(item)
                    TEST_DEQUE.appendleft(item)

                # 3. pop: 오른쪽 끝에서 요소 제거
                elif op == "pop":
                    ref_val = REFERENCE_DEQUE.pop()
                    test_val = TEST_DEQUE.pop()
                    self.assertEqual(ref_val, test_val)

                # 4. popleft: 왼쪽 끝에서 요소 제거
                elif op == "popleft":
                    ref_val = REFERENCE_DEQUE.popleft()
                    test_val = TEST_DEQUE.popleft()
                    self.assertEqual(ref_val, test_val)

                # 5. peek_front: 왼쪽 끝 요소 확인
                elif op == "peek_front":
                    ref_val = REFERENCE_DEQUE[0]
                    test_val = TEST_DEQUE.peek_front()
                    self.assertEqual(ref_val, test_val)

                # 6. peek_back: 오른쪽 끝 요소 확인
                elif op == "peek_back":
                    ref_val = REFERENCE_DEQUE[-1]
                    test_val = TEST_DEQUE.peek_back()
                    self.assertEqual(ref_val, test_val)

                # 7. empty: 비어있는지 비교
                elif op == "empty":
                    ref_val = (len(REFERENCE_DEQUE) == 0)
                    test_val = TEST_DEQUE.empty()
                    self.assertEqual(ref_val, test_val)

                # 8. size: 크기 비교
                elif op == "size":
                    ref_val = len(REFERENCE_DEQUE)
                    test_val = TEST_DEQUE.size()
                    self.assertEqual(ref_val, test_val)

            except Exception as e:
                self.fail(f"Operation '{op}' failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
    