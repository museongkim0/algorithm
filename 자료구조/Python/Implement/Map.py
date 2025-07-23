from ADT.ADTMap import ADTMap
from Implement.LinkedList import LinkedListTuple
from Implement.BinarySearchTree import BinarySearchTree
from Implement.Comparable import TupleKey
from typing import TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')

class LinkedListMap(ADTMap[K,V]):
    def __init__(self):
        self.list = LinkedListTuple[K, V]()

    # TODO: lower bound, upper bound / return을 optional로 하지 않고 index로 반환하는걸로 하는게 좋음
    def insert(self, key: K, val: V):
        index = self.list.search_insert_index(key)
        if index is None:
            self.list.append(key, val)
            return True
        if index[1] == key:
            self.list.replace(index[0], key, val)
            return False
        else:
            self.list.insert(index[0], key, val)
            return True


    def delete(self, key: K) -> bool:
        index = self.list.search_index(key)
        if index is None:
            return False
        self.list.erase(index)
        return True

    def get(self, key: K) -> Optional[V]:
        return self.list.search(key)

    def is_empty(self) -> bool:
        return self.list.get_size() == 0

    def get_size(self) -> int:
        return self.list.get_size()

    def display(self):
        return self.list.display()

# TODO: list -> tree로 변경 - done
# TODO: Cursur를 두면 효과적
class BinaryTreeMap(ADTMap[K,V]):
    def __init__(self):
        self.tree = BinarySearchTree[TupleKey[K, V]]()

    def insert(self, key: K, val: V):
        if self.tree.find(TupleKey((key, 0))) is not None:
            self.tree.insert(TupleKey((key, val)))
            return False
        self.tree.insert(TupleKey((key, val)))
        return True

    # TODO: 그냥 True로 변경 - done
    def delete(self, key: K) -> bool:
        if self.tree.find(TupleKey((key, 0))) is None:
            return False
        self.tree.erase(TupleKey((key, 0)))
        return True

    # TODO: find 결과 담아 놓으면 두번 필요x - done
    def get(self, key: K) -> Optional[V]:
        val = self.tree.find(TupleKey((key, 0)))
        if val is None:
            return None
        return val.get_data()[1]

    def is_empty(self) -> bool:
        return self.tree.get_size() == 0

    def get_size(self) -> int:
        return self.tree.get_size()

    def display(self):
        return self.tree.display()

# test_map = LinkedListMap()
# test_map = BinaryTreeMap[int, int]()
# print(test_map.get_size())
# print(test_map.is_empty())
# print(test_map.insert(1,1))
# print(test_map.insert(5,10))
# print(test_map.insert(3,20))
# print(test_map.insert(7,60))
# print(test_map.insert(5,30))
# print(test_map.get(5))
# print(test_map.get(10))
# print(test_map.delete(5))
# print(test_map.delete(10))
# print(test_map.get_size())
# print(test_map.is_empty())
# print(test_map.insert(2,100))
# print(test_map.display())
# print(test_map.insert(3,30))
# print(test_map.display())
# print(test_map.insert(100,20))
# print(test_map.display())
# print(test_map.get_size())
#
# test_dict = {(1,1), (2,100), (3,30), (5,30), (7,60), (100,20)}
# print(sorted(list(test_dict)) == test_map.display())