import random
import unittest
from Implement.LinkedListQueue import LinkedListQueue
from Implement.TwoStackQueue import TwoStackQueue

class TestQueue(unittest.TestCase):
    def test_random_operations(self):
        num_operations = 1000000  # 연산 횟수 (조정 가능)
        reference_queue = []  # 표준 파이썬 리스트 (큐로 사용, append와 pop(0)으로 시뮬레이션)
        # test_queue = LinkedListQueue()  # 테스트 대상 큐
        test_queue = TwoStackQueue()

        operations = ["push", "pop", "front", "back", "empty", "size"]

        for _ in range(num_operations):
            op = random.choice(operations)

            # 큐가 비었을 때 dequeue/peek 방지
            if op in ("pop", "front", "back") and len(reference_queue) == 0:
                continue

            try:
                # 1. enque: 랜덤 정수 추가
                if op == "push":
                    item = random.randint(-1000, 1000)
                    reference_queue.append(item)  # 큐의 끝에 추가
                    test_queue.push(item)
                    self.assertEqual(reference_queue, test_queue.display())

                # 2. dequeue: 결과값 비교
                elif op == "pop":
                    ref_val = reference_queue.pop(0)  # 큐의 맨 앞 제거
                    test_val = test_queue.pop()
                    self.assertEqual(ref_val, test_val)

                # 3. front: 값 비교 + 큐 변경 없음
                elif op == "front":
                    ref_val = reference_queue[0]  # 큐의 맨 앞 확인
                    test_val = test_queue.front()
                    self.assertEqual(ref_val, test_val)

                # 4. back: 값 비교 + 큐 변경 없음
                elif op == "back":
                    ref_val = reference_queue[-1]  # 큐의 맨 뒤뒤 확인
                    test_val = test_queue.back()
                    self.assertEqual(ref_val, test_val)

                # 5. empty: 비어있는지 비교
                elif op == "empty":
                    ref_val = (len(reference_queue) == 0)
                    test_val = test_queue.is_empty()
                    self.assertEqual(ref_val, test_val)

                # 6. size: 크기 비교
                elif op == "size":
                    ref_val = len(reference_queue)
                    test_val = test_queue.get_size()
                    self.assertEqual(ref_val, test_val)

            except Exception as e:
                self.fail(f"Operation '{op}' failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()