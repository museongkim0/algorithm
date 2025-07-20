from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')

class ADTBinarySearchTree(ABC, Generic[K,V]):
    @abstractmethod
    def front(self) -> Optional[tuple[K,V]]:
        # 트리의 최소값 반환
        pass

    @abstractmethod
    def back(self) -> Optional[tuple[K,V]]:
        # 트리의 최대값 반환
        pass

    @abstractmethod
    def find(self, key: K) -> Optional[tuple[K,V]]:
        # 특정 값의 노드 반환
        pass

    @abstractmethod
    def insert(self, key: K, val: V) -> None:
        # 특정 노드 삽입
        pass

    @abstractmethod
    def erase(self, key: K) -> Optional[tuple[K,V]]:
        # 특정 노드 삭제
        pass