from typing import TypeVar, Optional
from ADT.ADTBinaryHeap import ADTBinaryHeap
from Implement.BinaryTree import PointerBinaryTree, Node, ArrayBinaryTree
from collections import deque
from Implement.Comparable import TupleKey

T = TypeVar('T')


class BinaryHeap(ADTBinaryHeap[T]):
    def __init__(self):
        self.list = deque()
        # self.tree = PointerBinaryTree()
        # TODO: get_last_node, insert_last 등 구현
        self.tree = ArrayBinaryTree[T]()

    # def get_tree(self):
    #     return self.tree

    def push(self, data: T) -> None:
        # 새로운 값 삽입
        if self.tree.is_empty():
            self.tree.set_root(data)
            self.list.append([1, [self.tree.get_root()]])
            return
        last_level_list = self.list[-1]
        if len(last_level_list[1]) == 2**(last_level_list[0]-1):
            self.list.append([last_level_list[0]+1, []])
            last_level_list = self.list[-1]
        level = last_level_list[0]
        index = len(last_level_list[1])
        parent_node = self.list[level - 2][1][index // 2]
        if index % 2 == 0:
            self.tree.insert_left_child(parent_node, data)
            new_node = self.tree.get_left_child(parent_node)
        else:
            self.tree.insert_right_child(parent_node, data)
            new_node = self.tree.get_right_child(parent_node)
        self.__percolate_up(new_node)
        self.list[-1][1].append(new_node)

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
        data = self.tree.get_data(node)
        left_child_node = self.tree.get_left_child(node)
        if left_child_node is None:
            return
        left_child_data = self.tree.get_data(left_child_node)
        right_child_node = self.tree.get_right_child(node)
        if right_child_node is None:
            if left_child_data < data:
                left_child_node.set_data(data)
                node.set_data(left_child_data)
            return
        right_child_data = self.tree.get_data(right_child_node)
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

    def pop(self) -> Optional[T]:
        # 최소값/최대값 제거 후 반환
        pop_node = self.list[-1][1][-1]
        root_node = self.tree.get_root()
        pop_val = root_node.get_data()
        if pop_node is root_node:
            self.tree.set_root(None)
            self.list.pop()
            return pop_val
        root_node.set_data(pop_node.get_data())
        parent_node = pop_node.get_parent()
        if self.tree.get_left_child(parent_node) is pop_node:
            parent_node.set_left(None)
        elif self.tree.get_right_child(parent_node) is pop_node:
            parent_node.set_right(None)
        self.__percolate_down(root_node)
        self.list[-1][1].pop()
        if len(self.list[-1][1]) == 0:
            self.list.pop()
        return pop_val

    def peek(self) -> Optional[T]:
        # 최소값/최대값 반환
        return self.tree.get_root().get_data()

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
print(heap.peek())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.is_empty())




