from ADT.ADTMap import ADTMap
from Implement.LinkedList import LinkedListTuple
from Implement.BinarySearchTree import BinarySearchTreeTuple
from typing import TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')

class LinkedListMap(ADTMap[K,V]):
    def __init__(self):
        self.list = LinkedListTuple[int, int]()

    def insert(self, key: K, val: V):
        get_index = self.list.search_insert_index(key)
        if get_index is None:
            self.list.append(key, val)
            return True
        if get_index[1] == key:
            self.list.replace(get_index[0], key, val)
            return False
        else:
            self.list.insert(get_index[0], key, val)
            return True


    def delete(self, key: K) -> bool:
        get_index = self.list.search_index(key)
        if get_index is None:
            return False
        self.list.erase(get_index)
        return True

    def get(self, key: K) -> Optional[V]:
        return self.list.search(key)

    def is_empty(self) -> bool:
        return self.list.get_size() == 0

    def get_size(self) -> int:
        return self.list.get_size()

    def display(self):
        return self.list.display()

class BinaryTreeMap(ADTMap[K,V]):
    def __init__(self):
        self.list = BinarySearchTreeTuple()

    def insert(self, key: K, val: V):
        if self.list.find(key) is None:
            self.list.insert(key, val)
            return True
        else:
            self.list.insert(key, val)
            return False


    def delete(self, key: K) -> bool:
        if self.list.find(key) is None:
            return False
        return self.list.erase(key)[0] == key

    def get(self, key: K) -> Optional[V]:
        if self.list.find(key) is None:
            return None
        return self.list.find(key).get_data()[1]

    def is_empty(self) -> bool:
        return self.list.size() == 0

    def get_size(self) -> int:
        return self.list.size()

    def display(self):
        return self.list.display()

# test_map = LinkedListMap()
# test_map = BinaryTreeMap()
# print(test_map.get_size())
# print(test_map.is_empty())
# print(test_map.insert(1,1))
# test_map.display()
# print(test_map.insert(5,10))
# test_map.display()
# print(test_map.insert(3,20))
# test_map.display()
# print(test_map.insert(7,60))
# test_map.display()
# print(test_map.insert(5,30))
# test_map.display()
# print(test_map.get(5))
# print(test_map.get(10))
# print(test_map.delete(5))
# test_map.display()
# print(test_map.delete(10))
# test_map.display()
# print(test_map.get_size())
# print(test_map.is_empty())
# print(test_map.insert(2,100))
# print(test_map.display())
# print(test_map.insert(3,30))
# print(test_map.display())
# print(test_map.insert(100,20))
# print(test_map.display())

# import random
# test_dict = {}
#
# test_dict[1] = 10
# test_dict[5] = 20
# test_dict[3] = 30
# print(sorted(list(test_dict.items())))
# print(test_dict.pop(5))
# print(list(test_dict.items()))
# print(len(test_dict))
#
# print(random.choice(list(test_dict.keys())))