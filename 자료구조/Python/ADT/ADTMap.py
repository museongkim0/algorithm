from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

# 타입 변수 정의
K = TypeVar('K')
V = TypeVar('V')

class ADTMap(ABC, Generic[K,V]):
    @abstractmethod
    def insert(self, key: K, val: V) -> bool:
        # 특정 키/아이템 삽입, 새로운 아이템이면 true, 기존 아이템 수정이면 false
        pass

    @abstractmethod
    def delete(self, key: K) -> bool:
        # 특정 키 삭제
        pass

    @abstractmethod
    def get(self, key: K) -> Optional[V]:
        # 특정 키의 값 조회
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        # map이 비어있는지 여부
        pass

    @abstractmethod
    def get_size(self) -> int:
        # 크기 조회
        pass