"""validationのファイルを読み込む関数"""

from core.logger import log
from core.config import TARGETS
import os
import pytest


def read_file(file_path) -> list:
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        list: _description_
    """
    with open(file_path, encoding="utf-8") as file:
        ex_outputs = file.read().splitlines()
        log.info("ex outputs : %s", ex_outputs)

    return ex_outputs


def get_test_files(path, targets=TARGETS):  # pathディレクトリ内の全てのファイルを取得
    files = os.listdir(path)
    test_cases = []

    for file in files:
        # 拡張子が.inのファイルを探す
        if file.endswith(".in"):
            base_name = file[:-3]
            # 対応する.outファイルの存在を確認
            expected_file = base_name + ".out"
            if expected_file in files:
                # targetsに指定されている問題の場合のみテストケースに追加
                if path.split(os.path.sep)[-2] in targets:
                    test_cases.append(
                        pytest.param(
                            os.path.join(path, file),
                            os.path.join(path, expected_file),
                            id=base_name,
                        )
                    )
                else:
                    test_cases.append(
                        pytest.param(
                            os.path.join(path, file),
                            os.path.join(path, expected_file),
                            marks=pytest.mark.skip(reason="難易度が高いため"),
                            id=base_name,
                        )
                    )

    return test_cases
