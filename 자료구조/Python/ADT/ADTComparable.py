from typing import TypeVar, Generic, Optional, Tuple
from abc import ABC, abstractmethod
from functools import total_ordering

# 제네릭 타입 정의
K = TypeVar('K')  # 튜플의 첫 번째 값 (비교 기준)
V = TypeVar('V')  # 튜플의 두 번째 값
T = TypeVar('T', bound='Comparable')  # Comparable을 구현하는 제네릭 타입

# 비교 가능성을 위한 인터페이스
@total_ordering
class Comparable(ABC):
    @abstractmethod
    def __lt__(self, other) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass