from typing import TypeVar, Optional
from ADT.ADTBinarySearchTree import ADTBinarySearchTree
from Implement.BinaryTree import PointerBinaryTree

K = TypeVar('K')
V = TypeVar('V')

# TODO: Optional T -> K,V로 변경
class BinarySearchTree(ADTBinarySearchTree[K,V]):
    def __init__(self):
        self.tree = PointerBinaryTree[tuple[K,V]]()

    def front(self) -> Optional[tuple[K, V]]:
        if self.tree.is_empty():
            return None
        node = self.tree.get_root()
        # TODO: while True로 바꾸고 next에 None이면 멈추게 left_child를 두번 호출하는 것이 좋지 않음
        while True:
            next_node = self.tree.get_left_child(node)
            if next_node is None:
                return self.tree.get_data(node)
            node = next_node


    # TODO: get_edge_node(f) 형태로 front와 back의 유사한 로직을 파라미터로 조절
    def back(self) -> Optional[tuple[K, V]]:
        if self.tree.is_empty():
            return None
        node = self.tree.get_root()
        # TODO: while True로 바꾸고 next에 None이면 멈추게 right_child를 두번 호출하는 것이 좋지 않음
        while True:
            next_node = self.tree.get_right_child(node)
            if next_node is None:
                return self.tree.get_data(node)
            node = next_node

    def find(self, key: K) -> Optional[tuple[K,V]]:
        if self.tree.is_empty():
            return None
        return self.__find_recursive(self.tree.get_root(), key)

    def __find_recursive(self, node:Optional['Node[tuple[K, V]]'], key: K) -> Optional[tuple[K, V]]:
        if node is None:
            return None
        node_key = self.tree.get_data(node)[0]  # 키만 추출
        if node_key == key:
            return self.tree.get_data(node)
        elif node_key < key:
            return self.__find_recursive(self.tree.get_right_child(node), key)
        else:
            return self.__find_recursive(self.tree.get_left_child(node), key)

    def insert(self, key: K, val: V) -> None:
        if self.tree.is_empty():
            self.tree.set_root((key, val))
            return
        # TODO: find 중복 제거
        existing_node = self.__find_node(self.tree.get_root(), key)
        if existing_node and self.tree.get_data(existing_node)[0] == key:
            existing_node.set_data((key, val))
        else:
            self.__insert_recursive(self.tree.get_root(), key, val)

    def __find_node(self, node: Optional['Node[tuple[K, V]]'], key: K) -> Optional['Node[tuple[K, V]]']:
        if node is None:
            return None
        node_key = self.tree.get_data(node)[0]
        if node_key == key:
            return node
        elif node_key < key:
            return self.__find_node(self.tree.get_right_child(node), key)
        else:
            return self.__find_node(self.tree.get_left_child(node), key)

    # TODO: __find_recursive와 유사한 로직을 어떻게 공통화 시킬 수 있을지 고민 필요
    def __insert_recursive(self, node:Optional['Node[tuple[K, V]]'], key: K, val: V) -> None:
        node_key = self.tree.get_data(node)[0]
        if node_key < key:
            right_child = self.tree.get_right_child(node)
            if right_child is None:
                self.tree.insert_right_child(node, (key, val))
            else:
                self.__insert_recursive(right_child, key, val)
        else:
            left_child = self.tree.get_left_child(node)
            if left_child is None:
                self.tree.insert_left_child(node, (key, val))
            else:
                self.__insert_recursive(left_child, key, val)

    def erase(self, key: K) -> Optional[tuple[K,V]]:
        node = self.__find_node(self.tree.get_root(), key)
        return self.tree.remove_node(node)

    def size(self):
        return self.tree.get_size()

    def display(self) -> None:
        return self.tree.display()
        # self.tree.print_subtree(self.tree.get_root())

bst = BinarySearchTree()
bst.insert(30,1)
bst.insert(15,3)
bst.insert(20,3)
bst.insert(40,3)
bst.insert(100,3)
bst.insert(32,3)
bst.insert(36,3)
bst.insert(34,3)
bst.insert(38,3)
bst.insert(20,100)
print(bst.display())
print(bst.front())
print(bst.back())
print(bst.erase(30))
print(bst.erase(70))
print(bst.find(100))
print(bst.display())