from typing import TypeVar, Optional

from ADT.ADTBinaryTree import ADTBinaryTree
# T에 대한 부분 질문하기
T = TypeVar('T')

class PointerBinaryTree(ADTBinaryTree[T]):
    class Node:
        def __init__(self, data: T):
            self.parent = None
            self.data = data
            self.left = None
            self.right = None

        def get_data(self) -> T:
            return self.data

        def set_data(self, data: T):
            self.data = data

        def get_left(self) -> T:
            return self.left

        def set_left(self, node: T):
            self.left = node

        def get_right(self) -> T:
            return self.right

        def set_right(self, node: T):
            self.right = node

        def get_parent(self) -> T:
            return self.parent

        def set_parent(self, node: T):
            self.parent = node

    def __init__(self):
        self.root = None

    def set_root(self, data: T) -> None:
        self.root = self.Node(data)

    def get_root(self) -> Optional[T]:
        # 트리의 루트 노드를 반환
        return self.root

    def get_data(self, node: T) -> Optional[T]:
        # 특정 노드에 저장된 데이터를 반환
        if node is None:
            return None
        return node.get_data()

    def get_left_child(self, node: T) -> Optional[T]:
        # 특정 노드의 왼쪽 자식 노드를 반환
        if node is None:
            return None
        return node.get_left()

    def get_right_child(self, node: T) -> Optional[T]:
        # 특정 노드의 오른쪽 자식 노드를 반환
        if node is None:
            return None
        return node.get_right()

    def is_empty(self) -> bool:
        # 트리가 비어있는지 여부를 반환
        return self.root is None

    def insert_left_child(self, node: T, data: T) -> bool:
        # 주어진 parent_node의 왼쪽 자식으로 새 노드를 삽입 / 삽입 성공: True, 기존 노드가 있어 실패: False
        if self.is_empty() or node is None:
            return False
        if node.get_left() is not None:
            node.get_left().set_data(data)
        else:
            new_node = self.Node(data)
            node.set_left(new_node)
            new_node.set_parent(node)
        return True

    def insert_right_child(self, node: T, data: T) -> bool:
        # 주어진 parent_node의 오른쪽 자식으로 새 노드를 삽입
        if self.is_empty() or node is None:
            return False
        if node.get_right() is not None:
            node.get_right().set_data(data)
        else:
            new_node = self.Node(data)
            node.set_right(new_node)
            new_node.set_parent(node)
        return True

    def remove_node(self, node: T) -> Optional[T]:
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
            node.set_data(get_node.data)
            self.remove_node(get_node)
            return remove_data

    def get_size(self) -> int:
        # 트리에 포함된 전체 노드의 수를 반환
        return self.__get_recursive_size(self.root)

    def __get_recursive_size(self, node: T) -> int:
        if node is None:
            return 0
        return 1+self.__get_recursive_size(node.get_left())+self.__get_recursive_size(node.get_right())

    def get_height(self) -> int:
        # 트리의 깊이(또는 높이)를 반환 / 루트 노드부터 가장 깊은 리프 노드까지의 최대 간선 수를 의미
        return self.__get_recursive_height(self.root)

    def __get_recursive_height(self, node: T) -> int:
        if node is None:
            return 0
        if self.__get_recursive_height(node.get_left()) > self.__get_recursive_height(node.get_right()):
            return 1+self.__get_recursive_height(node.get_left())
        else:
            return 1+self.__get_recursive_height(node.get_right())


    def is_leaf(self, node: T) -> Optional[bool]:
        # 특정 노드가 리프 노드(자식 노드가 없는 노드)인지 여부를 반환
        if self.is_empty() or node is None:
            return None
        return node.get_left() is None and node.get_right() is None

    def __in_order(self, node: T, answer: []):
        if node is None:
            return
        self.__in_order(node.left, answer)
        answer.append(node.data)
        self.__in_order(node.right, answer)

    # 서브트리를 (간단하게) 출력하는 함수 (재귀)
    def print_subtree(self, node: Optional[Node], prefix: str = "", is_left: bool = True):
        if node is None:
            return

        if node.get_right():
            self.print_subtree(node.get_right(), prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))
        if node.get_left():
            self.print_subtree(node.get_left(), prefix + ("    " if is_left else "│   "), True)

    def display(self):
        answer = []
        self.__in_order(self.root, answer)
        return answer

class ArrayBinaryTree(ADTBinaryTree[T]):
    def __init__(self):
        self.list = [None]*100

    def set_root(self, data: T):
        self.list[1] = data

    def get_root(self) -> Optional[T]:
        # 트리의 루트 노드를 반환
        return 1

    def get_data(self, index: int) -> Optional[T]:
        # 특정 노드에 저장된 데이터를 반환
        if index < 1:
            return None
        return self.list[index]

    def get_left_child(self, index: int) -> Optional[T]:
        # 특정 노드의 왼쪽 자식 노드를 반환
        if index < 1:
            return None
        if self.list[2*index] is None:
            return None
        return 2*index

    def get_right_child(self, index: int) -> Optional[T]:
        # 특정 노드의 오른쪽 자식 노드를 반환
        if index < 1:
            return None
        if self.list[2*index+1] is None:
            return None
        return 2*index+1

    def is_empty(self) -> bool:
        # 트리가 비어있는지 여부를 반환
        return self.list[1] is None

    def insert_left_child(self, index: int, data: T) -> bool:
        # 주어진 parent_node의 왼쪽 자식으로 새 노드를 삽입 / 삽입 성공: True, 기존 노드가 있어 실패: False
        if self.is_empty() or index < 1:
            return False
        self.list[2*index] = data
        return True

    def insert_right_child(self, index: int, data: T) -> bool:
        # 주어진 parent_node의 오른쪽 자식으로 새 노드를 삽입
        if self.is_empty() or index < 1:
            return False
        self.list[2*index+1] = data
        return True

    # TODO: 배열 기반 삭제 질문
    def remove_node(self, index: int) -> Optional[T]:
        # 특정 노드를 트리에서 제거
        if index < 1:
            return None
        if self.is_leaf(index):
            self.list[index] = None
            return index
        # if self.list[2*index] is None and self.list[2*index+1] is not None:
        #     if index == 1:
        #         self.list = self.list[2*index:]
        #     else:
        #         node.get_right().set_parent(node.get_parent())
        #         parent = node.get_parent()
        #         if parent.get_left() == node:
        #             parent.set_left(node.get_right())
        #         if parent.get_right() == node:
        #             parent.set_right(node.get_right())
        #     return node
        # if self.list[2*index] is not None and self.list[2*index+1] is None:
        #     if node == self.root:
        #         node.get_left().set_parent(None)
        #         self.root = node.get_left()
        #     else:
        #         node.get_left().set_parent(node.get_parent())
        #         parent = node.get_parent()
        #         if parent.get_left() == node:
        #             parent.set_left(node.get_left())
        #         if parent.get_right() == node:
        #             parent.set_right(node.get_left())
        #     return node
        # if self.list[2*index] is not None and self.list[2*index+1] is not None:
        #     get_node = node.get_right()
        #     while get_node.get_left() is not None:
        #         get_node = get_node.get_left()
        #     node.set_data(get_node.data)
        #     self.remove_node(get_node)
        #     return node


    def get_size(self) -> int:
        # 트리에 포함된 전체 노드의 수를 반환
        return self.__get_recursive_size(1)

    def __get_recursive_size(self, index: int) -> int:
        if self.list[index] is None:
            return 0
        return 1+self.__get_recursive_size(2*index)+self.__get_recursive_size(2*index+1)

    def get_height(self) -> int:
        # 트리의 깊이(또는 높이)를 반환 / 루트 노드부터 가장 깊은 리프 노드까지의 최대 간선 수를 의미
        return self.__get_recursive_height(1)

    def __get_recursive_height(self, index: int) -> int:
        if self.list[index] is None:
            return 0
        if self.__get_recursive_height(2*index) > self.__get_recursive_height(2*index+1):
            return 1+self.__get_recursive_height(2*index)
        else:
            return 1+self.__get_recursive_height(2*index+1)


    def is_leaf(self, index: int) -> Optional[bool]:
        # 특정 노드가 리프 노드(자식 노드가 없는 노드)인지 여부를 반환
        if self.is_empty() or self.list[index] is None:
            return None
        return self.list[self.get_left_child(index)] is None and self.list[self.get_right_child(index)] is None

    # 서브트리를 (간단하게) 출력하는 함수 (재귀)
    def print_subtree(self, index: Optional[int], prefix: str = "", is_left: bool = True):
        if index is None:
            return

        if self.list[2*index+1] is not None:
            self.print_subtree(2*index+1, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(self.list[index]))
        if self.list[2*index] is not None:
            self.print_subtree(2*index, prefix + ("    " if is_left else "│   "), True)

# binary_tree = PointerBinaryTree()
# # binary_tree = ArrayBinaryTree()
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
# binary_tree.print_subtree(root)
# print(binary_tree.remove_node(root))
# binary_tree.print_subtree(root)
# print(binary_tree.get_data(root))
# binary_tree.insert_left_child(binary_tree.get_right_child(root), 7)
# binary_tree.insert_right_child(binary_tree.get_left_child(binary_tree.get_right_child(root)), 12)
# binary_tree.print_subtree(root)
# print(binary_tree.remove_node(root))
# binary_tree.print_subtree(root)
# print(binary_tree.get_size())
# print(binary_tree.get_height())
# print(binary_tree.is_leaf(binary_tree.get_right_child(binary_tree.get_left_child(root))))
# print(binary_tree.is_empty())