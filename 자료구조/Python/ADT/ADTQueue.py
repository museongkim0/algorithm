from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

# 타입 변수 정의
T = TypeVar('T')


class ADTQueue(ABC, Generic[T]):
    @abstractmethod
    def push(self, item: T) -> None:
        # 리스트 끝에 요소를 추가
        pass

    @abstractmethod
    def pop(self) -> Optional[T]:
        # 리스트 앞의 요소를 삭제
        pass

    @abstractmethod
    def front(self) -> Optional[T]:
        pass

    @abstractmethod
    def back(self) -> Optional[T]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass