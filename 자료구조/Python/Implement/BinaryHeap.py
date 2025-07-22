from typing import TypeVar, Optional
from ADT.ADTBinaryHeap import ADTBinaryHeap
from Implement.BinaryTree import PointerBinaryTree, Node
from collections import deque

T = TypeVar('T')

class BinaryHeap(ADTBinaryHeap[T]):
    def __init__(self):
        super().__init__(PointerBinaryTree[T]())
        self.list = deque()

    def push(self, data: T) -> None:
        # 새로운 값 삽입
        if self.tree.is_empty():
            self.tree.set_root(data)
            self.list.append(self.tree.get_root())
            return
        while True:
            node = self.list[0]
            if self.tree.is_leaf(node):
                self.__insert_node(node, data, "left")
                return
            if self.tree.get_left_child(node) is not None and self.tree.get_right_child(node) is None:
                self.__insert_node(node, data, "right")
                return
            self.list.popleft()

    def __insert_node(self, node: Optional['Node[T]'], data: T, mode: str) -> None:
        if mode == "right":
            self.tree.insert_right_child(node, data)
            new_node = self.tree.get_right_child(node)
            self.__percolate_up(new_node)
            self.list.append(new_node)
            return
        self.tree.insert_left_child(node, data)
        new_node = self.tree.get_left_child(node)
        self.__percolate_up(new_node)
        self.list.append(new_node)
        return

    def __percolate_up(self, node: Optional['Node[T]']) -> None:
        parent_node = node.get_parent()
        while parent_node is not None:
            parent_node_data = self.tree.get_data(parent_node)
            data = self.tree.get_data(node)
            if parent_node_data > data:
                parent_node.set_data(data)
                node.set_data(parent_node_data)
            node = parent_node
            parent_node = node.get_parent()

    def __percolate_down(self, node: Optional['Node[T]']) -> None:
        if node is None:
            return
        left_child_node = self.tree.get_left_child(node)
        right_child_node = self.tree.get_right_child(node)
        data = self.tree.get_data(node)
        if left_child_node is not None:
            left_child_data = self.tree.get_data(left_child_node)
            if left_child_data < data:
                left_child_node.set_data(data)
                node.set_data(left_child_data)
                self.__percolate_down(left_child_node)
                return
        if right_child_node is not None:
            right_child_data = self.tree.get_data(right_child_node)
            if right_child_data < data:
                right_child_node.set_data(data)
                node.set_data(right_child_data)
                self.__percolate_down(right_child_node)
                return
        return

    def pop(self) -> Optional[T]:
        # 최소값/최대값 제거 후 반환
        pop_node = self.__find_last()
        root_node = self.tree.get_root()
        pop_val = root_node.get_data()
        if pop_node is root_node:
            self.tree.set_root(None)
            return pop_val
        root_node.set_data(pop_node.get_data())
        parent_node = pop_node.get_parent()
        if self.tree.get_left_child(parent_node) is pop_node:
            parent_node.set_left(None)
        elif self.tree.get_right_child(parent_node) is pop_node:
            parent_node.set_right(None)
        self.__percolate_down(root_node)
        return pop_val

    def __find_last(self) -> Node[T]:
        bfs = deque()
        root_node = self.tree.get_root()
        bfs.append(root_node)
        pop_node = None
        while len(bfs) != 0:
            pop_node = bfs.popleft()
            left_child_node = self.tree.get_left_child(pop_node)
            right_child_node = self.tree.get_right_child(pop_node)
            if left_child_node is None and right_child_node is None:
                continue
            elif left_child_node is not None and right_child_node is None:
                bfs.append(left_child_node)
            elif left_child_node is not None and right_child_node is not None:
                bfs.append(left_child_node)
                bfs.append(right_child_node)
        return pop_node



    def peek(self) -> Optional[T]:
        # 최소값/최대값 반환
        return self.tree.get_root().get_data()

    def get_size(self) -> int:
        # 사이즈 반환
        return self.tree.get_size()

    def is_empty(self) -> bool:
        # 비어 있는지 여부 반환
        return self.tree.is_empty()

    def display(self):
        return self.tree.display()

# heap = BinaryHeap[int]()
# print(heap.is_empty())
# print(heap.get_size())
# print(heap.display())
# heap.push(303)
# print(heap.display())
# heap.push(159)
# print(heap.display())
# heap.push(7)
# print(heap.display())
# heap.push(6)
# print(heap.display())
# heap.push(20)
# print(heap.display())
# print(heap.is_empty())
# print(heap.get_size())
#
# print(heap.pop())
# print(heap.display())
# heap.push(3)
# print(heap.display())
# print(heap.peek())
# print(heap.pop())
# print(heap.pop())
# print(heap.pop())
# print(heap.pop())
# print(heap.pop())
# print(heap.is_empty())




