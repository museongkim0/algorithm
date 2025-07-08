from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

# 타입 변수 정의
T = TypeVar('T')

class ADTBinaryTree(ABC, Generic[T]):
    @abstractmethod
    def get_root(self) -> Optional[T]:
        # 트리의 루트 노드를 반환
        pass

    @abstractmethod
    def get_data(self, node: T) -> Optional[T]:
        # 특정 노드에 저장된 데이터를 반환
        pass

    @abstractmethod
    def get_left_child(self, node: T) -> Optional[T]:
        # 특정 노드의 왼쪽 자식 노드를 반환
        pass

    @abstractmethod
    def get_right_child(self, node: T) -> Optional[T]:
        # 특정 노드의 오른쪽 자식 노드를 반환
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        # 트리가 비어있는지 여부를 반환
        pass

    @abstractmethod
    def insert_left_child(self, node: T, data: T) -> bool:
        # 주어진 parent_node의 왼쪽 자식으로 새 노드를 삽입 / 삽입 성공: True, 기존 노드가 있어 실패: False
        pass

    @abstractmethod
    def insert_right_child(self, node: T, item: T) -> bool:
        # 주어진 parent_node의 오른쪽 자식으로 새 노드를 삽입
        pass

    @abstractmethod
    def remove_node(self, node:T) -> Optional[T]:
        # 특정 노드를 트리에서 제거
        pass

    @abstractmethod
    def get_size(self) -> int:
        # 트리에 포함된 전체 노드의 수를 반환
        pass

    @abstractmethod
    def get_height(self) -> int:
        # 트리의 깊이(또는 높이)를 반환 / 루트 노드부터 가장 깊은 리프 노드까지의 최대 간선 수를 의미
        pass

    @abstractmethod
    def is_leaf(self, node: T) -> Optional[bool]:
        # 특정 노드가 리프 노드(자식 노드가 없는 노드)인지 여부를 반환
        pass