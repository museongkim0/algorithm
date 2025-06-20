from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

# 타입 변수 정의
T = TypeVar('T')


class ADTLinkedList(ABC, Generic[T]):
    @abstractmethod
    def append(self, item: T) -> None:
        # 리스트 끝에 요소를 추가
        pass

    @abstractmethod
    def prepend(self, item: T) -> None:
        # 리스트 앞에 요소를 추가
        pass

    @abstractmethod
    def search(self, index: int) -> Optional[T]:
        # 특정 인덱스 탐색
        pass

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        pass

    @abstractmethod
    def replace(self, index: int, item: T) -> None:
        # 특정 인덱스 값 변경
        pass

    @abstractmethod
    def erase(self, index: int) -> Optional[T]:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass
