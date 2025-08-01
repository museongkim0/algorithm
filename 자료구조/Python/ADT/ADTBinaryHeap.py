from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional
from ADT.ADTBinaryTree import ADTBinaryTree

T = TypeVar('T')

class ADTBinaryHeap(ABC, Generic[T]):
    def __init__(self, tree: ADTBinaryTree[T]):
        self.tree = tree

    @abstractmethod
    def push(self, data: T) -> None:
        # 새로운 값 삽입
        pass

    @abstractmethod
    def pop(self) -> Optional[T]:
        # 최소값/최대값 제거 후 반환
        pass

    @abstractmethod
    def peek(self) -> Optional[T]:
        # 최소값/최대값 반환
        pass

    @abstractmethod
    def get_size(self) -> int:
        # 사이즈 반환
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        # 비어 있는지 여부 반환
        pass