from typing import TypeVar, Optional
from ADT.ADTBinaryHeap import ADTBinaryHeap
from Implement.BinaryTree import PointerBinaryTree, ArrayBinaryTree
from Implement.Comparable import TupleKey

T = TypeVar('T')


class BinaryHeap(ADTBinaryHeap[T]):
    def __init__(self):
        # self.tree = PointerBinaryTree()
        # TODO: get_last_node, insert_last 등 구현
        self.tree = ArrayBinaryTree[T]()

    def get_tree(self):
        return self.tree

    def push(self, data: T) -> None:
        # 새로운 값 삽입
        return super().push(data)

    def pop(self) -> Optional[T]:
        # 최소값/최대값 제거 후 반환
        return super().pop()

    def peek(self) -> Optional[T]:
        # 최소값/최대값 반환
        return super().peek()

    def get_size(self) -> int:
        return super().get_size()

    def is_empty(self) -> bool:
        # 비어 있는지 여부 반환
        return super().is_empty()

    def display(self):
        return self.tree.display()

heap = BinaryHeap[TupleKey[int, int]]()
print(heap.is_empty())
print(heap.get_size())
heap.push(TupleKey((303,50)))
print(heap.display())
heap.push(TupleKey((159, 100)))
print(heap.display())
heap.push(TupleKey((7,9)))
print(heap.display())
heap.push(TupleKey((6,10)))
print(heap.display())
heap.push(TupleKey((20,5)))
print(heap.display())
print(heap.is_empty())
print(heap.get_size())

print(heap.pop())
print(heap.display())
heap.push(TupleKey((3, 100)))
print(heap.display())
print("peek",heap.peek())
print(heap.pop())
print("--")
print(heap.display())
print(heap.pop())
print(heap.display())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.is_empty())




