"""標準出力のモック用の関数"""

from collections import deque
from .files import read_file
from typing import List


class In:
    """inputのmock"""

    def __init__(self, file_path: str) -> None:
        with open(file_path, encoding="utf-8") as file:
            self.__que: object = deque(file.readlines())

    def pop(self) -> str:
        """先頭データの取り出し。

        Returns:
            str: 先頭データ
        """
        return self.__que.popleft().strip()


class Out:
    """outputのmock"""

    def __init__(self, file_path: str) -> None:
        self.__outputs: List[str] = list()
        self.__validations: List[str] = read_file(file_path)

    def add(self, output: str) -> None:
        """標準出力の格納

        Args:
            output (str): 標準出力
        """
        if output != "\n":
            self.__outputs.append(output)

    @property
    def outputs(self) -> List[str]:
        """格納した標準出力の出力

        Returns:
            list: 標準出力格納用のリスト
        """
        outputs = list()
        pre_space_flag = True
        tmp_list = list()
        for output in self.__outputs:
            if output != " " and pre_space_flag:
                tmp_list.append(output)
                pre_space_flag = False

            elif output != " " and not pre_space_flag:
                outputs.append("".join(tmp_list))
                pre_space_flag = False
                tmp_list: List = list()
                tmp_list.append(output)

            elif output == " ":
                pre_space_flag = True
                tmp_list.append(output)
        outputs.append("".join(tmp_list))
        return outputs

    @property
    def validation(self) -> List[str]:
        return self.__validations
