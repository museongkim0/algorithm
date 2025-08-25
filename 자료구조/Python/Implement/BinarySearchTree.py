from typing import TypeVar, Optional
from ADT.ADTBinarySearchTree import ADTBinarySearchTree
from Implement.BinaryTree import PointerBinaryTree, ArrayBinaryTree
from Implement.Comparable import TupleKey

T = TypeVar('T')

class BinarySearchTree(ADTBinarySearchTree[T]):
    def __init__(self):
        # super().__init__(PointerBinaryTree[T]())
        super().__init__(ArrayBinaryTree[T]())

    def _get_edge_node(self, mode: str) -> Optional[T]:
        node = self.tree.get_root()
        # TODO: while True로 바꾸고 next에 None이면 멈추게 left_child를 두번 호출하는 것이 좋지 않음 - Done
        while True:
            if mode == "front":
                next_node = self.tree.get_left_child(node)
            else:
                next_node = self.tree.get_right_child(node)
            if next_node is None:
                return self.tree.get_data(node)
            node = next_node

    # TODO: get_edge_node(f) 형태로 front와 back의 유사한 로직을 파라미터로 조절 - Done
    def front(self) -> Optional[T]:
        if self.tree.is_empty():
            return None
        return self._get_edge_node("front")

    def back(self) -> Optional[T]:
        if self.tree.is_empty():
            return None
        return self._get_edge_node("back")

    def find(self, data: T) -> Optional[T]:
        if self.tree.is_empty():
            return None
        root = self.tree.get_root()
        return self.tree.get_data(self.__traverse(root, data, "find"))

    # def __find_node(self, node:T, data: T) -> Optional[T]:
    #     if node is None:
    #         return None
    #     if self.tree.get_data(node) == data:
    #         return node
    #     if self.tree.get_data(node) < data:
    #         return self.__find_node(self.tree.get_right_child(node), data)
    #     else:
    #         return self.__find_node(self.tree.get_left_child(node), data)

    def insert(self, data: T) -> None:
        if self.tree.is_empty():
            self.tree.set_root(data)
            return
        self.__traverse(self.tree.get_root(), data, "insert")

    def __traverse(self, node: Optional['PointerBinaryTree.Node[T]'], data: T, mode: str) -> Optional['PointerBinaryTree.Node[T]']:
        if node is None and mode == "find":
            return None
        node_data = self.tree.get_data(node)
        if node_data == data:
            if mode == "find":
                return node
            node.set_data(data)
            return None
        if node_data < data:
            next_node = self.tree.get_right_child(node)
            if mode == "insert" and next_node is None:
                self.tree.insert_right_child(node, data)
                return None
            return self.__traverse(next_node, data, mode)
        next_node = self.tree.get_left_child(node)
        if mode == "insert" and next_node is None:
            self.tree.insert_left_child(node, data)
            return None
        return self.__traverse(next_node, data, mode)

    # TODO: __find_node와 유사한 로직을 어떻게 공통화 시킬 수 있을지 고민 필요 - Done
    # def __insert_recursive(self, node: Optional['Node[T]'], data: T) -> None:
    #     node_data = self.tree.get_data(node)
    #     if node_data < data:
    #         right_child = self.tree.get_right_child(node)
    #         if right_child is None:
    #             self.tree.insert_right_child(node, data)
    #         else:
    #             self.__insert_recursive(right_child, data)
    #     else:
    #         left_child = self.tree.get_left_child(node)
    #         if left_child is None:
    #             self.tree.insert_left_child(node, data)
    #         else:
    #             self.__insert_recursive(left_child, data)


    def erase(self, data: T) -> Optional[T]:
        node = self.__traverse(self.tree.get_root(), data, "find")
        return self.tree.remove_node(node)

    def get_size(self) -> int:
        return self.tree.get_size()

    def display(self) -> None:
        return self.tree.display()
        # self.tree.print_subtree(self.tree.get_root())

# bst = BinarySearchTree[TupleKey[int, int]]()
# bst.insert(TupleKey((30,1)))
# bst.insert(TupleKey((15,3)))
# bst.insert(TupleKey((20,3)))
# bst.insert(TupleKey((40,3)))
# bst.insert(TupleKey((100,3)))
# bst.insert(TupleKey((32,3)))
# bst.insert(TupleKey((36,3)))
# bst.insert(TupleKey((34,3)))
# bst.insert(TupleKey((38,3)))
# bst.insert(TupleKey((20,100)))
# print(bst.display())
# print(bst.front())
# print(bst.back())
# # TODO: comparable 대용 TupleKey 사용시 key값으로만 비교하는 경우에도 value 값을 무조건 입력해야 하는 부분에 대한 보완점이 있는지 질문
# print(bst.erase(TupleKey((30, 0))))
# print(bst.erase(TupleKey((70, 0))))
# print(bst.find(TupleKey((100, 0))))
# print(bst.find(TupleKey((70, 0))))
# print(bst.display())
# print(bst.get_size())
# print(bst.find(TupleKey((32, 0))))

# K = TypeVar('K')
# V = TypeVar('V')
#
# # TODO: Optional T -> K,V로 변경
# class BinarySearchTree(ADTBinarySearchTree[K,V]):
#     def __init__(self):
#         self.tree = PointerBinaryTree[TupleKey[K,V]]()
#
#     def front(self) -> Optional[tuple[K, V]]:
#         if self.tree.is_empty():
#             return None
#         node = self.tree.get_root()
#         # TODO: while True로 바꾸고 next에 None이면 멈추게 left_child를 두번 호출하는 것이 좋지 않음
#         while True:
#             next_node = self.tree.get_left_child(node)
#             if next_node is None:
#                 return self.tree.get_data(node)
#             node = next_node
#
#
#     # TODO: get_edge_node(f) 형태로 front와 back의 유사한 로직을 파라미터로 조절
#     def back(self) -> Optional[tuple[K, V]]:
#         if self.tree.is_empty():
#             return None
#         node = self.tree.get_root()
#         # TODO: while True로 바꾸고 next에 None이면 멈추게 right_child를 두번 호출하는 것이 좋지 않음
#         while True:
#             next_node = self.tree.get_right_child(node)
#             if next_node is None:
#                 return self.tree.get_data(node)
#             node = next_node
#
#     def find(self, key: K) -> Optional[tuple[K,V]]:
#         if self.tree.is_empty():
#             return None
#         return self.__find_recursive(self.tree.get_root(), key)
#
#     def __find_recursive(self, node:Optional['Node[tuple[K, V]]'], key: K) -> Optional[tuple[K, V]]:
#         if node is None:
#             return None
#         node_key = self.tree.get_data(node)[0]  # 키만 추출
#         if node_key == key:
#             return self.tree.get_data(node)
#         elif node_key < key:
#             return self.__find_recursive(self.tree.get_right_child(node), key)
#         else:
#             return self.__find_recursive(self.tree.get_left_child(node), key)
#
#     def insert(self, key: K, val: V) -> None:
#         if self.tree.is_empty():
#             self.tree.set_root((key, val))
#             return
#         # TODO: find 중복 제거
#         existing_node = self.__find_node(self.tree.get_root(), key)
#         if existing_node and self.tree.get_data(existing_node)[0] == key:
#             existing_node.set_data((key, val))
#         else:
#             self.__insert_recursive(self.tree.get_root(), key, val)
#
#     def __find_node(self, node: Optional['Node[tuple[K, V]]'], key: K) -> Optional['Node[tuple[K, V]]']:
#         if node is None:
#             return None
#         node_key = self.tree.get_data(node)[0]
#         if node_key == key:
#             return node
#         elif node_key < key:
#             return self.__find_node(self.tree.get_right_child(node), key)
#         else:
#             return self.__find_node(self.tree.get_left_child(node), key)
#
#     def __insert_recursive(self, node:Optional['Node[tuple[K, V]]'], key: K, val: V) -> None:
#         node_key = self.tree.get_data(node)[0]
#         if node_key < key:
#             right_child = self.tree.get_right_child(node)
#             if right_child is None:
#                 self.tree.insert_right_child(node, (key, val))
#             else:
#                 self.__insert_recursive(right_child, key, val)
#         else:
#             left_child = self.tree.get_left_child(node)
#             if left_child is None:
#                 self.tree.insert_left_child(node, (key, val))
#             else:
#                 self.__insert_recursive(left_child, key, val)
#
#     def erase(self, key: K) -> Optional[tuple[K,V]]:
#         node = self.__find_node(self.tree.get_root(), key)
#         return self.tree.remove_node(node)
#
#     def size(self):
#         return self.tree.get_size()
#
#     def display(self) -> None:
#         return self.tree.display()
#         # self.tree.print_subtree(self.tree.get_root())