from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional
from ADT.ADTBinaryTree import ADTBinaryTree
from Implement.BinaryTree import Node

T = TypeVar('T')

class ADTBinaryHeap(ABC, Generic[T]):

    @abstractmethod
    def get_tree(self)-> ADTBinaryTree[T]:
        pass

    @abstractmethod
    def push(self, data: T) -> None:
        # 새로운 값 삽입
        self.get_tree().insert_last(data)
        self.__percolate_up(self.get_tree().get_last_node())

    @abstractmethod
    def pop(self) -> Optional[T]:
        # 최소값/최대값 제거 후 반환
        pop_node = self.get_tree().get_last_node()
        root_node = self.get_tree().get_root()
        pop_val = root_node.get_data()
        if pop_node.get_data() == root_node.get_data():
            self.get_tree().set_root(None)
            return pop_val
        root_node.set_data(pop_node.get_data())
        parent_node = pop_node.get_parent()
        if self.get_tree().get_left_child(parent_node).get_data() == pop_node.get_data():
            parent_node.set_left(None)
        elif self.get_tree().get_right_child(parent_node).get_data() == pop_node.get_data():
            parent_node.set_right(None)
        self.__percolate_down(root_node)
        return pop_val

    @abstractmethod
    def peek(self) -> Optional[T]:
        # 최소값/최대값 반환
        return self.get_tree().get_root().get_data()

    @abstractmethod
    def get_size(self) -> int:
        return self.get_tree().get_size()

    @abstractmethod
    def is_empty(self) -> bool:
        # 비어 있는지 여부 반환
        return self.get_tree().is_empty()

    def __percolate_up(self, node: Optional['Node[T]']) -> None:
        parent_node = node.get_parent()
        if parent_node is None:
            return
        while parent_node is not None:
            parent_node_data = self.get_tree().get_data(parent_node)
            data = self.get_tree().get_data(node)
            if parent_node_data > data:
                parent_node.set_data(data)
                node.set_data(parent_node_data)
            node = parent_node
            parent_node = node.get_parent()

    def __percolate_down(self, node: Optional['Node[T]']) -> None:
        data = self.get_tree().get_data(node)
        left_child_node = self.get_tree().get_left_child(node)
        if left_child_node is None:
            return
        left_child_data = self.get_tree().get_data(left_child_node)
        right_child_node = self.get_tree().get_right_child(node)
        if right_child_node is None:
            if left_child_data < data:
                left_child_node.set_data(data)
                node.set_data(left_child_data)
            return
        right_child_data = self.get_tree().get_data(right_child_node)
        if left_child_data < data and left_child_data <= right_child_data:
            left_child_node.set_data(data)
            node.set_data(left_child_data)
            self.__percolate_down(left_child_node)
            return
        elif right_child_data < data and right_child_data <= left_child_data:
            right_child_node.set_data(data)
            node.set_data(right_child_data)
            self.__percolate_down(right_child_node)
            return
        return