from typing import TypeVar, Generic, Tuple
from ADT.ADTComparable import Comparable

# 제네릭 타입 정의
K = TypeVar('K')  # 튜플의 첫 번째 값 (비교 기준)
V = TypeVar('V')  # 튜플의 두 번째 값
T = TypeVar('T', bound='Comparable')  # Comparable을 구현하는 제네릭 타입

# 튜플을 래핑하는 비교 가능 클래스
class TupleKey(Comparable, Generic[K, V]):
    def __init__(self, data: Tuple[K, V]):
        self.data = data

    def __lt__(self, other) -> bool:
        if not isinstance(other, TupleKey):
            return NotImplemented
        return self.data[0] < other.data[0]  # 튜플의 첫 번째 값을 기준으로 비교

    def __eq__(self, other) -> bool:
        if not isinstance(other, TupleKey):
            return NotImplemented
        return self.data[0] == other.data[0]  # 튜플의 첫 번째 값을 기준으로 비교

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)

    def get_data(self) -> Tuple[K, V]:
        return self.data