from typing import TypeVar, Optional

from ADT.ADTBinaryTree import ADTBinaryTree, Node
# T에 대한 부분 질문하기
T = TypeVar('T')

class PointerBinaryTree(ADTBinaryTree[T]):
    class Node(Node[T]):
        def __init__(self, data: T):
            self.parent = None
            self.data = data
            self.left = None
            self.right = None

        def get_data(self) -> T:
            return self.data

        def set_data(self, data: T) -> None:
            self.data = data

        def get_left(self) -> Optional[Node[T]]:
            return self.left

        def set_left(self, node: Optional[Node[T]]) -> None:
            self.left = node

        def get_right(self) -> Optional[Node[T]]:
            return self.right

        def set_right(self, node: Optional[Node[T]]) -> None:
            self.right = node

        def get_parent(self) -> Optional[Node[T]]:
            return self.parent

        def set_parent(self, node: Optional[Node[T]]) -> None:
            self.parent = node

    def __init__(self):
        self.root = None

    def create_node(self, data: T) -> Node[T]:
        return self.Node(data)

    def set_root(self, data: T) -> None:
        if data is None:
            self.root = None
            return
        self.root = self.Node(data)

    def get_root(self) -> Optional[Node[T]]:
        # 트리의 루트 노드를 반환
        return self.root

    def get_data(self, node: Node[T]) -> Optional[T]:
        # 특정 노드에 저장된 데이터를 반환
        return super().get_data(node)

    def get_left_child(self, node: Node[T]) -> Optional[Node[T]]:
        # 특정 노드의 왼쪽 자식 노드를 반환
        return super().get_left_child(node)

    def get_right_child(self, node: Node[T]) -> Optional[Node[T]]:
        # 특정 노드의 오른쪽 자식 노드를 반환
        return super().get_right_child(node)

    def is_empty(self) -> bool:
        # 트리가 비어있는지 여부를 반환
        return super().is_empty()

    def insert_left_child(self, node: Node[T], data: T) -> bool:
        # 주어진 parent_node의 왼쪽 자식으로 새 노드를 삽입 / 삽입 성공: True, 기존 노드가 있어 실패: False
        return super().insert_left_child(node, data)

    def insert_right_child(self, node: Node[T], data: T) -> bool:
        # 주어진 parent_node의 오른쪽 자식으로 새 노드를 삽입
        return super().insert_right_child(node, data)

    def remove_node(self, node: Node[T]) -> Optional[T]:
        # 특정 노드를 트리에서 제거
        if node is None:
            return None
        if self.is_leaf(node):
            if node == self.root:
                self.root = None
            else:
                parent = node.get_parent()
                if parent.get_left() == node:
                    parent.set_left(None)
                if parent.get_right() == node:
                    parent.set_right(None)
            return node.get_data()
        if node.get_left() is None and node.get_right() is not None:
            if node == self.root:
                node.get_right().set_parent(None)
                self.root = node.get_right()
            else:
                node.get_right().set_parent(node.get_parent())
                parent = node.get_parent()
                if parent.get_left() == node:
                    parent.set_left(node.get_right())
                if parent.get_right() == node:
                    parent.set_right(node.get_right())
            return node.get_data()
        if node.get_left() is not None and node.get_right() is None:
            if node == self.root:
                node.get_left().set_parent(None)
                self.root = node.get_left()
            else:
                node.get_left().set_parent(node.get_parent())
                parent = node.get_parent()
                if parent.get_left() == node:
                    parent.set_left(node.get_left())
                if parent.get_right() == node:
                    parent.set_right(node.get_left())
            return node.get_data()
        if node.get_left() is not None and node.get_right() is not None:
            get_node = node.get_right()
            while get_node.get_left() is not None:
                get_node = get_node.get_left()
            remove_data = node.get_data()
            node.set_data(get_node.get_data())
            self.remove_node(get_node)
            return remove_data

    def get_size(self) -> int:
        # 트리에 포함된 전체 노드의 수를 반환
        return super().get_size()

    def get_height(self) -> int:
        # 트리의 깊이(또는 높이)를 반환 / 루트 노드부터 가장 깊은 리프 노드까지의 최대 간선 수를 의미
        return super().get_height()

    def is_leaf(self, node: Node[T]) -> bool:
        # 특정 노드가 리프 노드(자식 노드가 없는 노드)인지 여부를 반환
        return super().is_leaf(node)

    def __in_order(self, node: T, answer: []):
        if node is None:
            return
        self.__in_order(node.left, answer)
        answer.append(node.data)
        self.__in_order(node.right, answer)

    def __pre_order(self, node: T, answer: []):
        if node is None:
            return
        answer.append(node.data)
        self.__pre_order(node.left, answer)
        self.__pre_order(node.right, answer)

    def display(self):
        # answer = []
        # self.__pre_order(self.root, answer)
        # # self.__in_order(self.root, answer)
        # return answer
        return self.print_subtree(self.root)

    # 서브트리를 (간단하게) 출력하는 함수 (재귀)
    def print_subtree(self, node: Optional[Node], prefix: str = "", is_left: bool = True):
        if node is None:
            return

        if node.get_right():
            self.print_subtree(node.get_right(), prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))
        if node.get_left():
            self.print_subtree(node.get_left(), prefix + ("    " if is_left else "│   "), True)


class ArrayBinaryTree(ADTBinaryTree[T]):
    class Node(Node[T]):
        def __init__(self, tree: 'ArrayBinaryTree[T]', index: int):
            self._tree = tree
            self._index = index

        def get_data(self) -> T:
            return self._tree.list[self._index]

        def set_data(self, data: T) -> None:
            self._tree.list[self._index] = data

        def get_left(self) -> Optional['ArrayBinaryTree.Node']:
            left_index = 2 * self._index
            if (left_index < len(self._tree.list) and
                    self._tree.list[left_index] is not None):
                return ArrayBinaryTree.Node(self._tree, left_index)
            return None

        def set_left(self, node: Optional['ArrayBinaryTree.Node']) -> None:
            # 배열 기반에서는 직접 set하지 않고 insert 메서드를 통해 처리
            if node is None:
                # 왼쪽 자식 삭제
                left_index = 2 * self._index
                if left_index < len(self._tree.list):
                    self._tree.list[left_index] = None
            else:
                # 새로운 노드의 데이터를 왼쪽 자식 위치에 복사
                left_index = 2 * self._index
                self._tree._ensure_capacity(left_index)
                self._tree.list[left_index] = node.get_data()

        def get_right(self) -> Optional['ArrayBinaryTree.Node']:
            right_index = 2 * self._index + 1
            if (right_index < len(self._tree.list) and
                    self._tree.list[right_index] is not None):
                return ArrayBinaryTree.Node(self._tree, right_index)
            return None

        def set_right(self, node: Optional['ArrayBinaryTree.Node']) -> None:
            # 배열 기반에서는 직접 set하지 않고 insert 메서드를 통해 처리
            if node is None:
                right_index = 2 * self._index + 1
                if right_index < len(self._tree.list):
                    self._tree.list[right_index] = None
            else:
                right_index = 2 * self._index + 1
                self._tree._ensure_capacity(right_index)
                self._tree.list[right_index] = node.get_data()

        def get_parent(self) -> Optional['ArrayBinaryTree.Node']:
            if self._index == 1:  # 루트 노드
                return None
            parent_index = self._index // 2
            if (parent_index >= 1 and
                    self._tree.list[parent_index] is not None):
                return ArrayBinaryTree.Node(self._tree, parent_index)
            return None

        def set_parent(self, node: Optional['ArrayBinaryTree.Node']) -> None:
            # 배열 기반에서는 부모-자식 관계가 인덱스로 고정되므로 변경 불가
            pass

        def get_index(self) -> int:
            """배열 기반 트리에서만 사용하는 헬퍼 메서드"""
            return self._index

    def __init__(self, initial_size: int = 100):
        self.list = [None] * initial_size

    def _ensure_capacity(self, index: int) -> None:
        """배열 크기가 부족하면 확장"""
        if index >= len(self.list):
            new_size = max(index + 1, len(self.list) * 2)
            new_list = [None] * new_size
            for i in range(len(self.list)):
                new_list[i] = self.list[i]
            self.list = new_list

    def create_node(self, data: T) -> Node[T]:
        # 임시 노드 생성 (실제 사용 시 인덱스 지정 필요)
        node = self.Node(self, 0)
        node.set_data(data)
        return node

    def set_root(self, data: T) -> None:
        self._ensure_capacity(1)
        self.Node(self,1).set_data(data)

    def get_root(self) -> Optional[Node[T]]:
        if self.list[1] is not None:
            return self.Node(self, 1)
        return None

    def get_data(self, node: Node[T]) -> Optional[T]:
        return super().get_data(node)

    def get_left_child(self, node: Node[T]) -> Optional[Node[T]]:
        return super().get_left_child(node)

    def get_right_child(self, node: Node[T]) -> Optional[Node[T]]:
        return super().get_right_child(node)

    def is_empty(self) -> bool:
        return super().is_empty()

    def insert_left_child(self, node: Node[T], data: T) -> bool:
        return super().insert_left_child(node, data)

    def insert_right_child(self, node: Node[T], data: T) -> bool:
        return super().insert_right_child(node, data)

    def remove_node(self, node: Node[T]) -> Optional[T]:
        if node is None or not isinstance(node, self.Node):
            return None

        index = node.get_index()
        if index >= len(self.list) or self.list[index] is None:
            return None

        removed_data = self.list[index]

        # 1. 리프 노드
        if self.is_leaf(node):
            self.list[index] = None
            return removed_data

        left_index = 2 * index
        right_index = 2 * index + 1
        has_left = (left_index < len(self.list) and self.list[left_index] is not None)
        has_right = (right_index < len(self.list) and self.list[right_index] is not None)

        # 2. 왼쪽 자식만 있는 경우: 왼쪽 서브트리를 현재 위치로 이동
        if has_left and not has_right:
            self._move_subtree_to_position(left_index, index)
            return removed_data

        # 3. 오른쪽 자식만 있는 경우: 오른쪽 서브트리를 현재 위치로 이동
        if not has_left and has_right:
            self._move_subtree_to_position(right_index, index)
            return removed_data

        # 4. 양쪽 자식 모두 있는 경우: successor로 교체 후 successor 삭제
        if has_left and has_right:
            successor_index = self._find_leftmost_in_subtree(right_index)
            self.list[index] = self.list[successor_index]
            successor_node = self.Node(self, successor_index)
            self.remove_node(successor_node)  # 재귀 삭제
            return removed_data

        return None

    def _find_leftmost_in_subtree(self, root_index: int) -> int:
        """서브트리에서 가장 왼쪽 노드의 인덱스 찾기 (inorder successor)"""
        current = root_index
        while (2 * current < len(self.list) and self.list[2 * current] is not None):
            current = 2 * current
        return current

    def _move_subtree_to_position(self, from_index: int, to_index: int) -> None:
        """서브트리를 특정 위치로 완전히 이동"""
        if from_index >= len(self.list) or self.list[from_index] is None:
            return

        # print(f"Moving subtree from index {from_index} to {to_index}")
        # print(f"Before move: {self.list}")

        # 1단계: 서브트리 전체 구조를 임시 저장
        subtree_data = self._extract_subtree(from_index)

        # print(f"Extracted subtree: {subtree_data}")

        # 2단계: 원본 서브트리 완전 삭제
        self._clear_subtree(from_index)

        # print(f"After clear: {self.list}")

        # 3단계: 새 위치에 서브트리 재구성
        self._rebuild_subtree_at_position(subtree_data, to_index)

        # print(f"After rebuild: {self.list}")

    def _extract_subtree(self, root_index: int) -> dict:
        """서브트리의 모든 데이터를 추출해서 딕셔너리로 반환"""
        if root_index >= len(self.list) or self.list[root_index] is None:
            return {}

        subtree = {}

        # BFS로 서브트리 전체를 탐색
        queue = [root_index]
        while queue:
            current_index = queue.pop(0)
            if current_index < len(self.list) and self.list[current_index] is not None:
                # 상대적 위치 계산 (root를 1로 정규화)
                relative_pos = self._get_relative_position(root_index, current_index)
                subtree[relative_pos] = self.list[current_index]

                # 자식들을 큐에 추가
                left_child = 2 * current_index
                right_child = 2 * current_index + 1

                if left_child < len(self.list) and self.list[left_child] is not None:
                    queue.append(left_child)
                if right_child < len(self.list) and self.list[right_child] is not None:
                    queue.append(right_child)

        return subtree

    def _get_relative_position(self, root_index: int, current_index: int) -> int:
        """루트를 기준으로 한 상대적 위치 계산"""
        if current_index == root_index:
            return 1  # 새로운 루트는 항상 1

        # 현재 인덱스가 루트로부터 어떤 경로에 있는지 계산
        path = []
        temp = current_index

        while temp != root_index:
            if temp % 2 == 0:  # 왼쪽 자식
                path.append('L')
                temp = temp // 2
            else:  # 오른쪽 자식
                path.append('R')
                temp = temp // 2

        # 경로를 역순으로 뒤집어서 새로운 위치 계산
        path.reverse()
        new_pos = 1
        for direction in path:
            if direction == 'L':
                new_pos = new_pos * 2
            else:  # 'R'
                new_pos = new_pos * 2 + 1

        return new_pos

    def _rebuild_subtree_at_position(self, subtree_data: dict, new_root_index: int) -> None:
        """추출한 서브트리 데이터를 새로운 위치에 재구성"""
        for relative_pos, data in subtree_data.items():
            # 상대적 위치를 절대적 위치로 변환
            if relative_pos == 1:
                actual_index = new_root_index
            else:
                # relative_pos를 경로로 변환해서 new_root_index 기준으로 실제 인덱스 계산
                actual_index = self._calculate_actual_index(new_root_index, relative_pos)

            self._ensure_capacity(actual_index)
            self.list[actual_index] = data

    def _calculate_actual_index(self, base_index: int, relative_pos: int) -> int:
        """상대적 위치를 실제 배열 인덱스로 변환"""
        if relative_pos == 1:
            return base_index

        # relative_pos를 이진 표현으로 변환해서 경로 추출
        # 예: relative_pos = 5 (101) -> 루트에서 L, R 경로
        path = []
        temp = relative_pos

        while temp > 1:
            if temp % 2 == 0:  # 왼쪽
                path.append('L')
                temp = temp // 2
            else:  # 오른쪽
                path.append('R')
                temp = temp // 2

        path.reverse()

        # 경로를 따라가며 실제 인덱스 계산
        current_index = base_index
        for direction in path:
            if direction == 'L':
                current_index = current_index * 2
            else:  # 'R'
                current_index = current_index * 2 + 1

        return current_index

    def _clear_subtree(self, index: int) -> None:
        """서브트리 완전 삭제 (개선된 버전)"""
        if index >= len(self.list) or self.list[index] is None:
            return

        # 자식들 먼저 재귀적으로 삭제
        left_child = 2 * index
        right_child = 2 * index + 1

        self._clear_subtree(left_child)
        self._clear_subtree(right_child)

        # 현재 노드 삭제
        self.list[index] = None

    def get_size(self) -> int:
        return super().get_size()

    def get_height(self) -> int:
        return super().get_height()

    def is_leaf(self, node: Node[T]) -> bool:
        return super().is_leaf(node)

    def display(self) -> None:
        # print(self.list[1:])
        self.print_subtree(1)

    def print_subtree(self, index: int, prefix: str = "", is_left: bool = True):
        if index >= len(self.list) or self.list[index] is None:
            return

        right_index = 2 * index + 1
        if (right_index < len(self.list) and self.list[right_index] is not None):
            self.print_subtree(right_index, prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(self.list[index]))

        left_index = 2 * index
        if (left_index < len(self.list) and self.list[left_index] is not None):
            self.print_subtree(left_index, prefix + ("    " if is_left else "│   "), True)

    def get_last_node(self):
        for i in range(1, len(self.list)):
            if self.list[i] is None:
                return self.Node(self, i-1)

    def insert_last(self, data: T):
        for i in range(1, len(self.list)):
            if self.list[i] is None:
                self.list[i] = data
                return
# binary_tree = PointerBinaryTree()
# binary_tree = ArrayBinaryTree()
# print(binary_tree.is_empty())
# binary_tree.set_root(5)
# root = binary_tree.get_root()
# print(root, binary_tree.get_data(root))
# print(binary_tree.insert_left_child(root, 1))
# binary_tree.insert_right_child(root, 2)
# binary_tree.insert_right_child(root, 6)
# binary_tree.insert_right_child(binary_tree.get_left_child(root), 3)
# binary_tree.insert_right_child(binary_tree.get_right_child(root), 4)
# binary_tree.insert_right_child(binary_tree.get_right_child(binary_tree.get_right_child(root)), 10)
# binary_tree.display()
# print(binary_tree.remove_node(root))
# binary_tree.display()
# print(binary_tree.get_data(root))
# binary_tree.insert_left_child(binary_tree.get_right_child(root), 7)
# binary_tree.insert_right_child(binary_tree.get_left_child(binary_tree.get_right_child(root)), 12)
# binary_tree.display()
# print(binary_tree.remove_node(root))
# binary_tree.display()
# print(binary_tree.get_size())
# print(binary_tree.get_height())
# print(binary_tree.is_leaf(binary_tree.get_right_child(binary_tree.get_left_child(root))))
# print(binary_tree.is_empty())
# print(binary_tree.remove_node(binary_tree.get_right_child(root)))
# binary_tree.display()