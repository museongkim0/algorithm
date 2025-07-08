import random
import unittest
from Implement.Map import LinkedListMap, BinaryTreeMap


def test_random_operations(tester, map):
    num_operations = 100000  # 연산 횟수 (조정 가능)
    reference_map = {}  # 표준 파이썬 리스트 (큐로 사용, append와 pop(0)으로 시뮬레이션)
    test_map = map  # 테스트 대상 큐

    operations = ["insert", "delete", "get", "empty", "size"]

    for _ in range(num_operations):
        op = random.choice(operations)

        # 큐가 비었을 때 dequeue/peek 방지
        if op in ("delete", "get") and len(reference_map) == 0:
            continue

        try:
            # 1. insert: 랜덤 key, val 추가
            if op == "insert":
                key = random.randint(0, 1000)
                val = random.randint(0, 1000)
                reference_map[key] = val  # 큐의 끝에 추가
                test_map.insert(key, val)
                tester.assertEqual(sorted(list(reference_map.items())), test_map.display())

            # 2. delete: 랜덤 key 값 삭제
            elif op == "delete":
                key = random.choice(list(reference_map.keys()))
                reference_map.pop(key)  # 큐의 맨 앞 제거
                test_map.delete(key)

            # 3. get: val 값 비교
            elif op == "get":
                key = random.choice(list(reference_map.keys()))
                ref_val = reference_map[key]  # 큐의 맨 앞 확인
                test_val = test_map.get(key)
                tester.assertEqual(ref_val, test_val)

            # 4. empty: 비어있는지 비교
            elif op == "empty":
                ref_val = (len(reference_map) == 0)
                test_val = test_map.is_empty()
                tester.assertEqual(ref_val, test_val)

            # 5. size: 크기 비교
            elif op == "size":
                ref_val = len(reference_map)
                test_val = test_map.get_size()
                tester.assertEqual(ref_val, test_val)

        except Exception as e:
            tester.fail(f"Operation '{op}' failed: {str(e)}")

class TestQueue(unittest.TestCase):
    def test_linked_list_map(self):
        test_random_operations(self, LinkedListMap())

    def test_binary_tree_map(self):
        test_random_operations(self, BinaryTreeMap())

if __name__ == "__main__":
    unittest.main()