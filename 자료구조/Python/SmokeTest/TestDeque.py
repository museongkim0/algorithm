import random
import unittest
from collections import deque
from Implement.Deque import LinkedListDeque


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
                    test_val = TEST_DEQUE.is_empty()
                    self.assertEqual(ref_val, test_val)

                # 8. size: 크기 비교
                elif op == "size":
                    ref_val = len(REFERENCE_DEQUE)
                    test_val = TEST_DEQUE.get_size()
                    self.assertEqual(ref_val, test_val)

            except Exception as e:
                self.fail(f"Operation '{op}' failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()