from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional
from ADT.ADTBinaryTree import ADTBinaryTree

T = TypeVar('T')

class ADTBinarySearchTree(ABC, Generic[T]):
    def __init__(self, tree: ADTBinaryTree[T]):
        self.tree = tree

    @abstractmethod
    def front(self) -> Optional[T]:
        # 트리의 최소값 반환
        pass

    @abstractmethod
    def back(self) -> Optional[T]:
        # 트리의 최대값 반환
        pass

    @abstractmethod
    def find(self, data: T) -> Optional[T]:
        # 특정 값의 노드 반환
        pass

    @abstractmethod
    def insert(self, data: T) -> None:
        # 특정 노드 삽입
        pass

    @abstractmethod
    def erase(self, data: T) -> Optional[T]:
        # 특정 노드 삭제
        pass

    @abstractmethod
    def get_size(self) -> int:
        # 트리의 크기 반환
        pass

# K = TypeVar('K')
# V = TypeVar('V')
#
# class ADTBinarySearchTree(ABC, Generic[K,V]):
#     @abstractmethod
#     def front(self) -> Optional[tuple[K,V]]:
#         # 트리의 최소값 반환
#         pass
#
#     @abstractmethod
#     def back(self) -> Optional[tuple[K,V]]:
#         # 트리의 최대값 반환
#         pass
#
#     @abstractmethod
#     def find(self, key: K) -> Optional[tuple[K,V]]:
#         # 특정 값의 노드 반환
#         pass
#
#     @abstractmethod
#     def insert(self, key: K, val: V) -> None:
#         # 특정 노드 삽입
#         pass
#
#     @abstractmethod
#     def erase(self, key: K) -> Optional[tuple[K,V]]:
#         # 특정 노드 삭제
#         pass