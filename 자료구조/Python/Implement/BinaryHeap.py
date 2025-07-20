from typing import TypeVar, Optional
from ADT.ADTBinaryHeap import ADTBinaryHeap
from Implement.BinaryTree import PointerBinaryTree

T = TypeVar('T')

class BinaryHeap(ADTBinaryHeap[T]):
    def __init__(self):
        super().__init__(PointerBinaryTree())

    def push(self, data: T) -> None:
        # 새로운 값 삽입
        if self.tree.is_empty():
            self.tree.set_root(data)
        root = self.tree.get_root()
        node = self.__find_node(root)

    def __find_node(self, node):
        if self.tree.is_leaf(node):
            return node.get_left_child()

    def pop(self) -> Optional[T]:
        # 최소값/최대값 제거 후 반환
        pass

    def peek(self) -> Optional[T]:
        # 최소값/최대값 반환
        return self.tree.get_root().get_data()

    def get_size(self) -> int:
        # 사이즈 반환
        return self.tree.get_size()

    def is_empty(self) -> bool:
        # 비어 있는지 여부 반환
        return self.tree.is_empty()
