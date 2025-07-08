from typing import TypeVar, Optional

from ADT.ADTBinarySearchTree import ADTBinarySearchTree, ADTBinarySearchTreeTuple
from Implement.BinaryTree import PointerBinaryTree

T = TypeVar('T')

class BinarySearchTree(ADTBinarySearchTree[T]):
    def __init__(self):
        self.tree = PointerBinaryTree()

    def front(self) -> Optional[T]:
        if self.tree.is_empty():
            return None
        node = self.tree.get_root()
        while self.tree.get_left_child(node):
            node = self.tree.get_left_child(node)
        return self.tree.get_data(node)


    def back(self) -> Optional[T]:
        if self.tree.is_empty():
            return None
        node = self.tree.get_root()
        while self.tree.get_right_child(node):
            node = self.tree.get_right_child(node)
        return self.tree.get_data(node)

    def find(self, data: T) -> Optional[T]:
        if self.tree.is_empty():
            return None
        root = self.tree.get_root()
        return self.__find_recursive(root, data)

    def __find_recursive(self, node:T, data: T) -> Optional[T]:
        if node is None:
            return None
        if self.tree.get_data(node) == data:
            return node
        if self.tree.get_data(node) < data:
            return self.__find_recursive(self.tree.get_right_child(node), data)
        else:
            return self.__find_recursive(self.tree.get_left_child(node), data)

    def insert(self, data: T) -> None:
        if self.tree.is_empty():
            self.tree.set_root(data)
            return
        root = self.tree.get_root()
        self.__insert_recursive__(root, data)

    def __insert_recursive__(self, node:T, data: T) -> None:
        if self.tree.get_data(node) < data:
            if self.tree.get_right_child(node) is None:
                self.tree.insert_right_child(node, data)
            else:
                self.__insert_recursive__(self.tree.get_right_child(node), data)
        else:
            if self.tree.get_left_child(node) is None:
                self.tree.insert_left_child(node, data)
            else:
                self.__insert_recursive__(self.tree.get_left_child(node), data)


    def erase(self, data: T) -> Optional[T]:
        return self.tree.get_data(self.tree.remove_node(self.find(data)))

    def display(self) -> None:
        self.tree.print_subtree(self.tree.get_root())

K = TypeVar('K')
V = TypeVar('V')

class BinarySearchTreeTuple(ADTBinarySearchTreeTuple[K,V]):
    def __init__(self):
        self.tree = PointerBinaryTree()

    def front(self) -> Optional[T]:
        if self.tree.is_empty():
            return None
        node = self.tree.get_root()
        while self.tree.get_left_child(node):
            node = self.tree.get_left_child(node)
        return self.tree.get_data(node)


    def back(self) -> Optional[T]:
        if self.tree.is_empty():
            return None
        node = self.tree.get_root()
        while self.tree.get_right_child(node):
            node = self.tree.get_right_child(node)
        return self.tree.get_data(node)

    def find(self, key: K) -> Optional[T]:
        if self.tree.is_empty():
            return None
        root = self.tree.get_root()
        return self.__find_recursive(root, key)

    def __find_recursive(self, node:T, key: K) -> Optional[T]:
        if node is None:
            return None
        if self.tree.get_data(node)[0] == key:
            return node
        if self.tree.get_data(node)[0] < key:
            return self.__find_recursive(self.tree.get_right_child(node), key)
        else:
            return self.__find_recursive(self.tree.get_left_child(node), key)

    def insert(self, key: K, val: V) -> None:
        if self.tree.is_empty():
            self.tree.set_root((key, val))
            return
        if self.find(key) is not None:
            self.find(key).set_data((key,val))
            return
        root = self.tree.get_root()
        self.__insert_recursive__(root, key, val)

    def __insert_recursive__(self, node:T, key: K, val: V) -> None:
        if self.tree.get_data(node)[0] < key:
            if self.tree.get_right_child(node) is None:
                self.tree.insert_right_child(node, (key, val))
            else:
                self.__insert_recursive__(self.tree.get_right_child(node), key, val)
        else:
            if self.tree.get_left_child(node) is None:
                self.tree.insert_left_child(node, (key, val))
            else:
                self.__insert_recursive__(self.tree.get_left_child(node), key, val)


    def erase(self, key: K) -> Optional[T]:
        return self.tree.remove_node(self.find(key))

    def size(self):
        return self.tree.get_size()

    def display(self) -> None:
        return self.tree.display()
        # self.tree.print_subtree(self.tree.get_root())

# bst = BinarySearchTreeTuple()
# bst.insert(30,1)
# bst.insert(15,3)
# bst.insert(20,3)
# bst.insert(40,3)
# bst.insert(100,3)
# bst.insert(32,3)
# bst.insert(36,3)
# bst.insert(34,3)
# bst.insert(38,3)
# bst.insert(20,100)
# bst.display()
# print(bst.front())
# print(bst.back())
# print(bst.erase(30))
# print(bst.erase(70))
# print(bst.find(100))
# bst.display()