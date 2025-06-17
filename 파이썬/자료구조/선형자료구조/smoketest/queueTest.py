from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
import random
import unittest
from linked_list import LinkedList

T = TypeVar('T')

class AbstractQueue(ABC, Generic[T]):
    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def front(self) -> T:
        pass
    
    @abstractmethod
    def back(self) -> T:
        pass

    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass


class LinkedListQueue(AbstractQueue[T]):
    def __init__(self) -> None:
        # TODO
        self.list = LinkedList()
        pass

    def push(self, item: T) -> None:
        # TODO
        self.list.append(item)
        pass

    def pop(self) -> T:
        # TODO
        answer = self.list.eraseFirst()
        if answer is None:
            raise IndexError("Queue is empty")
        else:
            return answer
        
    def front(self) -> T:
        # TODO
        answer = self.list.findFirst()
        if answer is None:
            raise IndexError("Queue is empty")
        else:
            return answer
        
    def back(self) -> T:
        # TODO
        answer = self.list.findLast()
        if answer is None:
            raise IndexError("Queue is empty")
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

class TestQueue(unittest.TestCase):
    def test_random_operations(self):
        NUM_OPERATIONS = 1000000  # 연산 횟수 (조정 가능)
        REFERENCE_QUEUE = []     # 표준 파이썬 리스트 (큐로 사용, append와 pop(0)으로 시뮬레이션)
        TEST_QUEUE = LinkedListQueue()  # 테스트 대상 큐

        OPERATIONS = ["push", "pop", "front", "back", "empty", "size"]

        for _ in range(NUM_OPERATIONS):
            op = random.choice(OPERATIONS)

            # 큐가 비었을 때 dequeue/peek 방지
            if op in ("pop", "front", "back") and len(REFERENCE_QUEUE) == 0:
                continue

            try:
                # 1. enque: 랜덤 정수 추가
                if op == "push":
                    item = random.randint(-1000, 1000)
                    REFERENCE_QUEUE.append(item)  # 큐의 끝에 추가
                    TEST_QUEUE.push(item)

                # 2. dequeue: 결과값 비교
                elif op == "pop":
                    ref_val = REFERENCE_QUEUE.pop(0)  # 큐의 맨 앞 제거
                    test_val = TEST_QUEUE.pop()
                    self.assertEqual(ref_val, test_val)

                # 3. front: 값 비교 + 큐 변경 없음
                elif op == "front":
                    ref_val = REFERENCE_QUEUE[0]  # 큐의 맨 앞 확인
                    test_val = TEST_QUEUE.front()
                    self.assertEqual(ref_val, test_val)
                    
                # 4. back: 값 비교 + 큐 변경 없음
                elif op == "back":
                    ref_val = REFERENCE_QUEUE[-1]  # 큐의 맨 뒤뒤 확인
                    test_val = TEST_QUEUE.back()
                    self.assertEqual(ref_val, test_val)

                # 5. empty: 비어있는지 비교
                elif op == "empty":
                    ref_val = (len(REFERENCE_QUEUE) == 0)
                    test_val = TEST_QUEUE.empty()
                    self.assertEqual(ref_val, test_val)
                
                # 6. size: 크기 비교
                elif op == "size":
                    ref_val = len(REFERENCE_QUEUE)
                    test_val = TEST_QUEUE.size()
                    self.assertEqual(ref_val, test_val)

            except Exception as e:
                self.fail(f"Operation '{op}' failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()