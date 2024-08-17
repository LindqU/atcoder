import os
from core import In, Out
from core import get_test_files
from .main import main
import pytest

test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")


@pytest.mark.parametrize("_input, _expected", get_test_files(test_dir))
def test_main(monkeypatch: pytest.MonkeyPatch, _input, _expected):
    stdin: In = In(_input)
    stdout: Out = Out(_expected)
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout._Out__outputs == stdout.validation