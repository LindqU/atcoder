from sys import stdin
from enum import Enum
from typing import Tuple, Union
from abc import ABC, abstractmethod
from enum import Enum


# Enum 定義
class Actions(Enum):
    INCREMENT = 1
    DECREMENT = 2
    OUTPUT = 3


# インターフェース定義
class ActionHandler(ABC):
    @abstractmethod
    def execute(self, value: Tuple[dict[int, int], int]) -> dict[int, int]:
        pass


# 具体的なクラス定義
class IncrementAction(ActionHandler):
    def execute(self, value: Tuple[dict[int, int], int]) -> dict[int, int]:
        if value[1] in value[0]:
            value[0][value[1]] += 1
        else:
            value[0][value[1]] = 1
        return value[0]


class DecrementAction(ActionHandler):
    def execute(self, value: Tuple[dict[int, int], int]) -> dict[int, int]:
        value[0][value[1]] -= 1
        if value[0][value[1]] == 0:
            del value[0][value[1]]
        return value[0]


class OutputAction(ActionHandler):
    def execute(self, value: Tuple[dict[int, int], int]) -> dict[int, int]:
        print(len(value[0]))
        return value[0]


# ActionTypeとクラスをマッピング
action_map = {
    Actions.INCREMENT: IncrementAction(),
    Actions.DECREMENT: DecrementAction(),
    Actions.OUTPUT: OutputAction(),
}


def main():
    _input = stdin.readline
    Q = int(_input().strip())
    _map = {}

    for _ in range(Q):
        query = _input().strip()
        if len(query) > 1:
            action_type, num = map(int, query.split(" "))
        else:
            action_type, num = int(query), 0
        action_enum = Actions(action_type)
        handler = action_map[action_enum]
        _map = handler.execute((_map, num))


if __name__ == "__main__":
    main()
