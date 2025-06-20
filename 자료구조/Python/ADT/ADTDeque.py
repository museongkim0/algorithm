from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

# 타입 변수 정의
T = TypeVar('T')

class ADTDeque(ABC, Generic[T]):
    @abstractmethod
    def append(self, item: T) -> None:
        # 리스트 뒤에 요소를 추가
        pass

    def appendleft(self, item: T) -> None:
        # 리스트 앞에 요소를 추가
        pass

    @abstractmethod
    def pop(self) -> Optional[T]:
        # 리스트 뒤의 요소를 삭제
        pass

    @abstractmethod
    def popleft(self) -> Optional[T]:
        # 리스트 앞의 요소를 삭제
        pass

    @abstractmethod
    def peek_front(self) -> Optional[T]:
        pass

    @abstractmethod
    def peek_back(self) -> Optional[T]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass