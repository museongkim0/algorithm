from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Node(ABC, Generic[T]):
    @abstractmethod
    def get_data(self) -> T:
        pass

    @abstractmethod
    def set_data(self, data: T) -> None:
        pass

    @abstractmethod
    def get_left(self) -> Optional['Node[T]']:
        pass

    @abstractmethod
    def set_left(self, node: Optional['Node[T]']) -> None:
        pass

    @abstractmethod
    def get_right(self) -> Optional['Node[T]']:
        pass

    @abstractmethod
    def set_right(self, node: Optional['Node[T]']) -> None:
        pass

    @abstractmethod
    def get_parent(self) -> Optional['Node[T]']:
        pass

    @abstractmethod
    def set_parent(self, node: Optional['Node[T]']) -> None:
        pass

# TODO: 노드도 인터페이스로 생성 가능
class ADTBinaryTree(ABC, Generic[T]):
    @abstractmethod
    def get_root(self) -> Optional[Node[T]]:
        # 트리의 루트 노드를 반환
        pass

    @abstractmethod
    def set_root(self, data: T) -> None:
        # 트리의 루트 노드를 저장
        pass

    @abstractmethod
    def get_data(self, node: Node[T]) -> Optional[T]:
        # 특정 노드에 저장된 데이터를 반환
        pass

    @abstractmethod
    def get_left_child(self, node: Node[T]) -> Optional[Node[T]]:
        # 특정 노드의 왼쪽 자식 노드를 반환
        pass

    @abstractmethod
    def get_right_child(self, node: Node[T]) -> Optional[Node[T]]:
        # 특정 노드의 오른쪽 자식 노드를 반환
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        # 트리가 비어있는지 여부를 반환
        pass

    @abstractmethod
    def insert_left_child(self, node: Node[T], data: T) -> bool:
        # 주어진 parent_node의 왼쪽 자식으로 새 노드를 삽입 / 삽입 성공: True, 기존 노드가 있어 실패: False
        pass

    @abstractmethod
    def insert_right_child(self, node: Node[T], data: T) -> bool:
        # 주어진 parent_node의 오른쪽 자식으로 새 노드를 삽입
        pass

    # TODO: Generic 다시 검토
    @abstractmethod
    def remove_node(self, node: Node[T]) -> Optional[T]:
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

    # TODO: 반환에 왜 optional 인지 고민 필요
    @abstractmethod
    def is_leaf(self, node: Node[T]) -> bool:
        # 특정 노드가 리프 노드(자식 노드가 없는 노드)인지 여부를 반환
        pass