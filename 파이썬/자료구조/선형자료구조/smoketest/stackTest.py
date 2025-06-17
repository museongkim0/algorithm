from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
import random
import unittest
from linked_list import LinkedList

T = TypeVar('T')

class AbstractStack(ABC, Generic[T]):
    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def peek(self) -> T:
        pass

    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass


class LinkedListStack(AbstractStack[T]):
    def __init__(self) -> None:
        # TODO
        self.list = LinkedList()
        pass

    def push(self, item: T) -> None:
        # TODO
        self.list.preAppend(item)
        pass

    def pop(self) -> T:
        # TODO
        findNode = self.list.findFirst()
        if not findNode:
            return None
        else:
            self.list.erase(findNode)
        return findNode.data

    def peek(self) -> T:
        # TODO
        if not self.list.findFirst():
            return None
        else:
            return self.list.findFirst().data

    def empty(self) -> bool:
        # TODO
        if self.list.size == 0:
            return True
        else:
            return False

    def size(self) -> int:
        # TODO
        return self.list.size


class TestStack(unittest.TestCase):
    def test_random_operations(self):
        NUM_OPERATIONS = 1000000  # 연산 횟수 (조정 가능)
        REFERENCE_STACK = []     # 표준 파이썬 리스트 (스택으로 사용)
        TEST_STACK = LinkedListStack()  # 테스트 대상 스택

        OPERATIONS = ["push", "pop", "peek", "empty", "size"]

        for _ in range(NUM_OPERATIONS):
            op = random.choice(OPERATIONS)

            # 스택이 비었을 때 pop/peek 방지
            if op in ("pop", "peek") and len(REFERENCE_STACK) == 0:
                continue

            try:
                # 1. 푸시: 랜덤 정수 추가
                if op == "push":
                    item = random.randint(-1000, 1000)
                    REFERENCE_STACK.append(item)
                    TEST_STACK.push(item)

                # 2. 팝: 결과값 비교
                elif op == "pop":
                    ref_val = REFERENCE_STACK.pop()
                    test_val = TEST_STACK.pop()
                    self.assertEqual(ref_val, test_val)

                # 3. 피크: 값 비교 + 스택 변경 없음
                elif op == "peek":
                    ref_val = REFERENCE_STACK[-1]
                    test_val = TEST_STACK.peek()
                    self.assertEqual(ref_val, test_val)

                # 4. empty: 비어있는지지 비교
                elif op == "empty":
                    ref_val = (len(REFERENCE_STACK) == 0)
                    test_val = TEST_STACK.empty()
                    self.assertEqual(ref_val, test_val)
                
                # 5. size: 크기기 비교
                elif op == "size":
                    ref_val = len(REFERENCE_STACK)
                    test_val = TEST_STACK.size()
                    self.assertEqual(ref_val, test_val)

            except Exception as e:
                self.fail(f"Operation '{op}' failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
