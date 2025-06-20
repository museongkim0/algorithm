import random
import unittest
from Implement.LinkedListStack import LinkedListStack


class TestStack(unittest.TestCase):
    def test_random_operations(self):
        num_operations = 1000000  # 연산 횟수 (조정 가능)
        reference_stack = []  # 표준 파이썬 리스트 (스택으로 사용)
        test_stack = LinkedListStack()  # 테스트 대상 스택

        operations = ["push", "pop", "peek", "empty", "size"]

        # count = 0
        for _ in range(num_operations):
            # count += 1
            # print(count)
            op = random.choice(operations)

            # 스택이 비었을 때 pop/peek 방지
            if op in ("pop", "peek") and len(reference_stack) == 0:
                continue

            try:
                # 1. 푸시: 랜덤 정수 추가
                if op == "push":
                    item = random.randint(-1000, 1000)
                    reference_stack.append(item)
                    test_stack.push(item)

                # 2. 팝: 결과값 비교
                elif op == "pop":
                    ref_val = reference_stack.pop()
                    test_val = test_stack.pop()
                    self.assertEqual(ref_val, test_val)

                # 3. 피크: 값 비교 + 스택 변경 없음
                elif op == "peek":
                    ref_val = reference_stack[-1]
                    test_val = test_stack.top()
                    self.assertEqual(ref_val, test_val)

                # 4. empty: 비어있는지지 비교
                elif op == "empty":
                    ref_val = (len(reference_stack) == 0)
                    test_val = test_stack.is_empty()
                    self.assertEqual(ref_val, test_val)

                # 5. size: 크기기 비교
                elif op == "size":
                    ref_val = len(reference_stack)
                    test_val = test_stack.get_size()
                    self.assertEqual(ref_val, test_val)

            except Exception as e:
                self.fail(f"Operation '{op}' failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
