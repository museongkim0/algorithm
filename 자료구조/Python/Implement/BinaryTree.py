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
        self.size = 0

    def set_root(self, data: T) -> None:
        if data is None:
            self.root = None
            self.size = 0
            return
        self.root = self.Node(data)
        self.size += 1

    def get_root(self) -> Optional[Node[T]]:
        # 트리의 루트 노드를 반환
        return self.root

    def get_data(self, node: Node[T]) -> Optional[T]:
        # 특정 노드에 저장된 데이터를 반환
        if node is None:
            return None
        return node.get_data()

    def get_left_child(self, node: Node[T]) -> Optional[Node[T]]:
        # 특정 노드의 왼쪽 자식 노드를 반환
        if node is None:
            return None
        return node.get_left()

    def get_right_child(self, node: Node[T]) -> Optional[Node[T]]:
        # 특정 노드의 오른쪽 자식 노드를 반환
        if node is None:
            return None
        return node.get_right()

    def is_empty(self) -> bool:
        # 트리가 비어있는지 여부를 반환
        return self.root is None

    def insert_left_child(self, node: Node[T], data: T) -> bool:
        # 주어진 parent_node의 왼쪽 자식으로 새 노드를 삽입 / 삽입 성공: True, 기존 노드가 있어 실패: False
        if self.is_empty() or node is None:
            return False
        if node.get_left() is not None:
            node.get_left().set_data(data)
        else:
            new_node = self.Node(data)
            node.set_left(new_node)
            new_node.set_parent(node)
            self.size += 1
        return True

    def insert_right_child(self, node: Node[T], data: T) -> bool:
        # 주어진 parent_node의 오른쪽 자식으로 새 노드를 삽입
        if self.is_empty() or node is None:
            return False
        if node.get_right() is not None:
            node.get_right().set_data(data)
        else:
            new_node = self.Node(data)
            node.set_right(new_node)
            new_node.set_parent(node)
            self.size += 1
        return True

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
        # return self.size
        return self.__get_recursive_size(self.root)

    def __get_recursive_size(self, node: Node[T]) -> int:
        if node is None:
            return 0
        return 1+self.__get_recursive_size(node.get_left())+self.__get_recursive_size(node.get_right())

    def get_height(self) -> int:
        # 트리의 깊이(또는 높이)를 반환 / 루트 노드부터 가장 깊은 리프 노드까지의 최대 간선 수를 의미
        return self.__get_recursive_height(self.root)

    def __get_recursive_height(self, node: Node[T]) -> int:
        if node is None:
            return 0
        if self.__get_recursive_height(node.get_left()) > self.__get_recursive_height(node.get_right()):
            return 1+self.__get_recursive_height(node.get_left())
        else:
            return 1+self.__get_recursive_height(node.get_right())


    def is_leaf(self, node: Node[T]) -> bool:
        # 특정 노드가 리프 노드(자식 노드가 없는 노드)인지 여부를 반환
        if self.is_empty() or node is None:
            return False
        return node.get_left() is None and node.get_right() is None

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

# # TODO: 사이즈 변수 사용하면 재귀를 매번 하지 않아도 됨
# class ArrayBinaryTree(ADTBinaryTree[T]):
#     def __init__(self):
#         self.list = [None]*100
#
#     def set_root(self, data: T):
#         self.list[1] = data
#
#     def get_root(self) -> Optional[T]:
#         # 트리의 루트 노드를 반환
#         return 1
#
#     def get_data(self, index: int) -> Optional[T]:
#         # 특정 노드에 저장된 데이터를 반환
#         if index < 1:
#             return None
#         return self.list[index]
#
#     def get_left_child(self, index: int) -> Optional[T]:
#         # 특정 노드의 왼쪽 자식 노드를 반환
#         if index < 1:
#             return None
#         if self.list[2*index] is None:
#             return None
#         return 2*index
#
#     def get_right_child(self, index: int) -> Optional[T]:
#         # 특정 노드의 오른쪽 자식 노드를 반환
#         if index < 1:
#             return None
#         if self.list[2*index+1] is None:
#             return None
#         return 2*index+1
#
#     def is_empty(self) -> bool:
#         # 트리가 비어있는지 여부를 반환
#         return self.list[1] is None
#
#     def insert_left_child(self, index: int, data: T) -> bool:
#         # 주어진 parent_node의 왼쪽 자식으로 새 노드를 삽입 / 삽입 성공: True, 기존 노드가 있어 실패: False
#         if self.is_empty() or index < 1:
#             return False
#         self.list[2*index] = data
#         return True
#
#     def insert_right_child(self, index: int, data: T) -> bool:
#         # 주어진 parent_node의 오른쪽 자식으로 새 노드를 삽입
#         if self.is_empty() or index < 1:
#             return False
#         self.list[2*index+1] = data
#         return True
#
#     # TODO: 배열 기반 삭제 질문
#     # TODO: 재귀로 구현
#     def remove_node(self, index: int) -> Optional[T]:
#         # 특정 노드를 트리에서 제거
#         if index < 1:
#             return None
#         if self.is_leaf(index):
#             self.list[index] = None
#             return index
#         if self.list[2*index] is None and self.list[2*index+1] is not None:
#             if index == 1:
#                 self.list = self.list[2*index:]
#
#     def get_size(self) -> int:
#         # 트리에 포함된 전체 노드의 수를 반환
#         return self.__get_recursive_size(1)
#
#     def __get_recursive_size(self, index: int) -> int:
#         if self.list[index] is None:
#             return 0
#         return 1+self.__get_recursive_size(2*index)+self.__get_recursive_size(2*index+1)
#
#     def get_height(self) -> int:
#         # 트리의 깊이(또는 높이)를 반환 / 루트 노드부터 가장 깊은 리프 노드까지의 최대 간선 수를 의미
#         return self.__get_recursive_height(1)
#
#     def __get_recursive_height(self, index: int) -> int:
#         if self.list[index] is None:
#             return 0
#         # TODO: 함수 중복 계산 두번 비효율 -> 변수로 변경
#         left_height = self.__get_recursive_height(2*index)
#         right_height = self.__get_recursive_height(2*index+1)
#         if left_height > right_height:
#             return 1+left_height
#         else:
#             return 1+right_height
#
#     def is_leaf(self, index: int) -> bool:
#         # 특정 노드가 리프 노드(자식 노드가 없는 노드)인지 여부를 반환
#         if self.is_empty() or self.list[index] is None:
#             return False
#         return self.list[self.get_left_child(index)] is None and self.list[self.get_right_child(index)] is None
#
#     # 서브트리를 (간단하게) 출력하는 함수 (재귀)
#     def print_subtree(self, index: Optional[int], prefix: str = "", is_left: bool = True):
#         if index is None:
#             return
#
#         if self.list[2*index+1] is not None:
#             self.print_subtree(2*index+1, prefix + ("│   " if is_left else "    "), False)
#         print(prefix + ("└── " if is_left else "┌── ") + str(self.list[index]))
#         if self.list[2*index] is not None:
#             self.print_subtree(2*index, prefix + ("    " if is_left else "│   "), True)

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
            pass

        def get_right(self) -> Optional['ArrayBinaryTree.Node']:
            right_index = 2 * self._index + 1
            if (right_index < len(self._tree.list) and
                    self._tree.list[right_index] is not None):
                return ArrayBinaryTree.Node(self._tree, right_index)
            return None

        def set_right(self, node: Optional['ArrayBinaryTree.Node']) -> None:
            # 배열 기반에서는 직접 set하지 않고 insert 메서드를 통해 처리
            pass

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
        self.size = 0

    def _ensure_capacity(self, index: int) -> None:
        """배열 크기가 부족하면 확장"""
        if index >= len(self.list):
            new_size = max(index + 1, len(self.list) * 2)
            new_list = [None] * new_size
            for i in range(len(self.list)):
                new_list[i] = self.list[i]
            self.list = new_list

    def set_root(self, data: T) -> None:
        self._ensure_capacity(1)
        if self.list[1] is None:
            self.size += 1
        self.list[1] = data

    def get_root(self) -> Optional[Node[T]]:
        if self.list[1] is not None:
            return self.Node(self, 1)
        return None

    def get_data(self, node: Node[T]) -> Optional[T]:
        if node is None or not isinstance(node, self.Node):
            return None
        return node.get_data()

    def get_left_child(self, node: Node[T]) -> Optional[Node[T]]:
        if node is None or not isinstance(node, self.Node):
            return None
        return node.get_left()

    def get_right_child(self, node: Node[T]) -> Optional[Node[T]]:
        if node is None or not isinstance(node, self.Node):
            return None
        return node.get_right()

    def is_empty(self) -> bool:
        return self.size == 0

    def insert_left_child(self, node: Node[T], data: T) -> bool:
        if self.is_empty() or node is None or not isinstance(node, self.Node):
            return False

        left_index = 2 * node.get_index()
        self._ensure_capacity(left_index)

        if self.list[left_index] is not None:
            self.list[left_index] = data
            return False
        self.list[left_index] = data
        self.size += 1
        return True

    def insert_right_child(self, node: Node[T], data: T) -> bool:
        if self.is_empty() or node is None or not isinstance(node, self.Node):
            return False

        right_index = 2 * node.get_index() + 1
        self._ensure_capacity(right_index)

        if self.list[right_index] is not None:
            self.list[right_index] = data
            return False
        self.list[right_index] = data
        self.size += 1
        return True

    # def remove_node(self, node: Node[T]) -> Optional[T]:
    #     # 포인터 기반 트리와 동일한 로직
    #     if node is None or not isinstance(node, self.Node):
    #         return None
    #
    #     index = node.get_index()
    #     if self.list[index] is None:
    #         return None
    #
    #     # 리프 노드인 경우
    #     if self.is_leaf(node):
    #         data = self.list[index]
    #         self.list[index] = None
    #         self.size -= 1
    #         return data
    #
    #     # 오른쪽 자식만 있는 경우
    #     left_index = 2 * index
    #     right_index = 2 * index + 1
    #     has_left = (left_index < len(self.list) and self.list[left_index] is not None)
    #     has_right = (right_index < len(self.list) and self.list[right_index] is not None)
    #
    #     if not has_left and has_right:
    #         data = self.list[index]
    #         # 오른쪽 서브트리를 현재 위치로 이동
    #         self._move_subtree(right_index, index)
    #         self.size -= 1
    #         return data
    #
    #     # 왼쪽 자식만 있는 경우
    #     if has_left and not has_right:
    #         data = self.list[index]
    #         # 왼쪽 서브트리를 현재 위치로 이동
    #         self._move_subtree(left_index, index)
    #         self.size -= 1
    #         return data
    #
    #     # 양쪽 자식이 모두 있는 경우
    #     if has_left and has_right:
    #         # 오른쪽 서브트리에서 가장 작은 값 찾기 (successor)
    #         successor_index = right_index
    #         while (2 * successor_index < len(self.list) and
    #                self.list[2 * successor_index] is not None):
    #             successor_index = 2 * successor_index
    #
    #         # 현재 노드의 데이터 저장
    #         removed_data = self.list[index]
    #
    #         # successor의 데이터로 현재 노드 교체
    #         self.list[index] = self.list[successor_index]
    #
    #         # successor 노드 제거 (재귀 호출)
    #         successor_node = self.Node(self, successor_index)
    #         self.remove_node(successor_node)
    #
    #         return removed_data
    #
    #     return None

    def remove_node(self, node: Node[T]) -> Optional[T]:
        if node is None or not isinstance(node, self.Node):
            return None

        index = node.get_index()
        if self.list[index] is None:
            return None

        removed_data = self.list[index]

        # 1. 리프 노드인 경우
        if self.is_leaf(node):
            self.list[index] = None
            self.size -= 1
            return removed_data

        left_index = 2 * index
        right_index = 2 * index + 1
        has_left = (left_index < len(self.list) and self.list[left_index] is not None)
        has_right = (right_index < len(self.list) and self.list[right_index] is not None)

        # 2. 오른쪽 자식만 있는 경우
        if not has_left and has_right:
            # 배열 기반에서는 직접 서브트리를 이동할 수 없으므로
            # 루트가 아닌 경우 부모와의 연결을 고려해야 함
            if index == 1:  # 루트 노드인 경우
                self._move_subtree(right_index, index)
            else:
                # 부모의 자식 포인터를 오른쪽 자식으로 변경하고 서브트리 이동
                parent_index = index // 2
                if 2 * parent_index == index:  # 왼쪽 자식이었다면
                    self._move_subtree(right_index, index)
                else:  # 오른쪽 자식이었다면
                    self._move_subtree(right_index, index)
            self.size -= 1
            return removed_data

        # 3. 왼쪽 자식만 있는 경우
        if has_left and not has_right:
            if index == 1:  # 루트 노드인 경우
                self._move_subtree(left_index, index)
            else:
                self._move_subtree(left_index, index)
            self.size -= 1
            return removed_data

        # 4. 양쪽 자식이 모두 있는 경우 - 여기가 핵심 수정 부분!
        if has_left and has_right:
            # 오른쪽 서브트리에서 가장 작은 값(successor) 찾기
            # PointerBinaryTree와 동일한 로직: 오른쪽으로 가서 계속 왼쪽으로
            successor_index = right_index
            while (2 * successor_index < len(self.list) and
                   self.list[2 * successor_index] is not None):
                successor_index = 2 * successor_index

            # successor의 데이터로 현재 노드 교체
            self.list[index] = self.list[successor_index]

            # successor 노드 제거 (재귀 호출)
            # 이때 size는 재귀 호출에서 감소되므로 여기서는 건드리지 않음
            successor_node = self.Node(self, successor_index)
            self.remove_node(successor_node)

            return removed_data

        return None

    def _move_subtree(self, from_index: int, to_index: int) -> None:
        """서브트리를 from_index에서 to_index로 이동 - 수정된 버전"""
        if from_index >= len(self.list) or self.list[from_index] is None:
            if to_index < len(self.list):
                self.list[to_index] = None
            return

        # 현재 노드 이동
        self._ensure_capacity(to_index)
        self.list[to_index] = self.list[from_index]

        # 원본 위치는 None으로 설정 (단, to_index와 같지 않은 경우에만)
        if from_index != to_index:
            self.list[from_index] = None

        # 왼쪽 자식 이동
        from_left = 2 * from_index
        to_left = 2 * to_index
        if from_left < len(self.list) and self.list[from_left] is not None:
            self._move_subtree(from_left, to_left)

        # 오른쪽 자식 이동
        from_right = 2 * from_index + 1
        to_right = 2 * to_index + 1
        if from_right < len(self.list) and self.list[from_right] is not None:
            self._move_subtree(from_right, to_right)
    #
    # def _move_subtree(self, from_index: int, to_index: int) -> None:
    #     """서브트리를 from_index에서 to_index로 이동"""
    #     if from_index >= len(self.list) or self.list[from_index] is None:
    #         if to_index < len(self.list):
    #             self.list[to_index] = None
    #         return
    #
    #     # 현재 노드 이동
    #     self._ensure_capacity(to_index)
    #     self.list[to_index] = self.list[from_index]
    #     self.list[from_index] = None
    #
    #     # 왼쪽 자식 이동
    #     from_left = 2 * from_index
    #     to_left = 2 * to_index
    #     if from_left < len(self.list):
    #         self._move_subtree(from_left, to_left)
    #
    #     # 오른쪽 자식 이동
    #     from_right = 2 * from_index + 1
    #     to_right = 2 * to_index + 1
    #     if from_right < len(self.list):
    #         self._move_subtree(from_right, to_right)

    def get_size(self) -> int:
        return len([i for i in self.list[1:] if i is not None])
        # return self.size

    def get_height(self) -> int:
        if self.is_empty():
            return -1
        return self.__get_recursive_height(1)

    def __get_recursive_height(self, index: int) -> int:
        if index >= len(self.list) or self.list[index] is None:
            return -1

        left_height = self.__get_recursive_height(2 * index)
        right_height = self.__get_recursive_height(2 * index + 1)

        return max(left_height, right_height) + 1

    def is_leaf(self, node: Node[T]) -> bool:
        if not isinstance(node, self.Node) or self.is_empty():
            return False

        index = node.get_index()
        left_index = 2 * index
        right_index = 2 * index + 1

        left_exists = (left_index < len(self.list) and
                       self.list[left_index] is not None)
        right_exists = (right_index < len(self.list) and
                        self.list[right_index] is not None)

        return not left_exists and not right_exists

    def display(self) -> None:
        print([i for i in self.list[1:] if i is not None])
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
# binary_tree.print_subtree(root.get_index())
# print(binary_tree.remove_node(root))
# binary_tree.print_subtree(root.get_index())
# print(binary_tree.get_data(root))
# binary_tree.insert_left_child(binary_tree.get_right_child(root), 7)
# binary_tree.insert_right_child(binary_tree.get_left_child(binary_tree.get_right_child(root)), 12)
# binary_tree.print_subtree(root.get_index())
# print(binary_tree.remove_node(root))
# binary_tree.print_subtree(root.get_index())
# print(binary_tree.get_size())
# print(binary_tree.get_height())
# print(binary_tree.is_leaf(binary_tree.get_right_child(binary_tree.get_left_child(root))))
# print(binary_tree.is_empty())
# print(binary_tree.remove_node(binary_tree.get_right_child(root)))
# binary_tree.print_subtree(root.get_index())