import random
import unittest
from Implement.LinkedList import LinkedList, DoubleLinkedList

def test_random_operations(tester, linked_list):
    print("linked_list: ", linked_list)
    num_operations = 1000  # 연산 횟수 (조정 가능)
    referebce_list = []  # 표준 파이썬 리스트 (리스트로 사용)
    # test_linked_list = LinkedList()  # 테스트 대상 링크드 리스트
    # test_linked_list = DoubleLinkedList()
    test_linked_list = linked_list

    operations = ["append", "prepend", "search", "insert", "replace", "erase"]

    # count = 0
    for _ in range(num_operations):
        # count += 1
        # print(count)
        op = random.choice(operations)

        # 큐가 비었을 때 dequeue/peek 방지
        if op in ("search", "replace", "erase") and len(referebce_list) == 0:
            continue

        try:
            # 1. append: 랜덤 정수 리스트 끝에 추가
            if op == "append":
                item = random.randint(-1000, 1000)
                referebce_list.append(item)
                test_linked_list.append(item)
                tester.assertEqual(referebce_list, test_linked_list.display())

            # 2. prepend: 랜덤 정수 리스트 앞에 추가
            elif op == "prepend":
                item = random.randint(-1000, 1000)
                referebce_list.insert(0, item)
                test_linked_list.prepend(item)
                tester.assertEqual(referebce_list, test_linked_list.display())

            # 3. search: 탐색 결과값 비교
            elif op == "search":
                index = random.randint(0, len(referebce_list) - 1)
                ref_val = referebce_list[index]
                test_val = test_linked_list.search(index)
                tester.assertEqual(ref_val, test_val)

            # 4. insert: 값 비교
            elif op == "insert":
                index = random.randint(0, len(referebce_list))
                item = random.randint(-1000, 1000)
                referebce_list.insert(index, item)
                test_linked_list.insert(index, item)
                tester.assertEqual(referebce_list, test_linked_list.display())

            # 5. replace: 값 비교 + 큐 변경 없음
            elif op == "replace":
                index = random.randint(0, len(referebce_list) - 1)
                item = random.randint(-1000, 1000)
                referebce_list[index] = item
                test_linked_list.replace(index, item)
                tester.assertEqual(referebce_list, test_linked_list.display())

            # 6. erase: 비어있는지 비교
            elif op == "erase":
                index = random.randint(0, len(referebce_list) - 1)
                ref_val = referebce_list.pop(index)
                test_val = test_linked_list.erase(index)
                tester.assertEqual(ref_val, test_val)

            # 7. size: 크기 비교
            elif op == "size":
                ref_val = len(referebce_list)
                test_val = test_linked_list.get_size()
                tester.assertEqual(ref_val, test_val)

        except Exception as e:
            tester.fail(f"Operation '{op}' failed: {str(e)}")

class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        test_random_operations(self, LinkedList())

    def test_double_linked_list(self):
        test_random_operations(self, DoubleLinkedList())


if __name__ == "__main__":
    unittest.main()