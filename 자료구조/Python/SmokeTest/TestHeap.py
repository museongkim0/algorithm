import random
import unittest
from Implement.BinaryHeap import BinaryHeap
import heapq

def test_random_operations(tester, input_heap):
    num_operations = 100000  # 연산 횟수 (조정 가능)
    reference_heap = [] # 표준 파이썬 힙
    heapq.heapify(reference_heap)
    test_heap = input_heap  # 테스트 대상 큐

    operations = ["push", "pop", "peek", "empty", "size"]

    for _ in range(num_operations):
        op = random.choice(operations)

        # 큐가 비었을 때 dequeue/peek 방지
        if op in ("pop", "peek") and len(reference_heap) == 0:
            continue

        try:
            # 1. push: 랜덤 val 추가
            if op == "push":
                val = random.randint(0, 1000)
                heapq.heappush(reference_heap, val)
                test_heap.push(val)
                # tester.assertEqual(sorted(list(reference_map.items())), test_map.display())

            # 2. pop: 최소 값 삭제
            elif op == "pop":
                ref_val = heapq.heappop(reference_heap)  # 큐의 맨 앞 제거
                test_val = test_heap.pop()
                tester.assertEqual(ref_val, test_val)

            # 3. peek: 루트 값 비교
            elif op == "peek":
                ref_val = reference_heap[0]  # 큐의 맨 앞 확인
                test_val = test_heap.peek()
                tester.assertEqual(ref_val, test_val)

            # 4. empty: 비어있는지 비교
            elif op == "empty":
                ref_val = (len(reference_heap) == 0)
                test_val = test_heap.is_empty()
                tester.assertEqual(ref_val, test_val)

            # 5. size: 크기 비교
            elif op == "size":
                ref_val = len(reference_heap)
                test_val = test_heap.get_size()
                tester.assertEqual(ref_val, test_val)

        except Exception as e:
            tester.fail(f"Operation '{op}' failed: {str(e)}")

class TestHeap(unittest.TestCase):
    def test_binary_tree_heap(self):
        test_random_operations(self, BinaryHeap())

if __name__ == "__main__":
    unittest.main()