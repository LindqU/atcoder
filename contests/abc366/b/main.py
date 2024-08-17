from sys import stdin


def main():
    _input = stdin.readline
    N: int = int(_input().strip())
    S: list[str] = []
    max_len: int = 0

    for _ in range(N):
        s = _input().strip()
        S.append(s)
        if len(s) > max_len:
            max_len = len(s)
    
    _list = []
    for _ in range(max_len):
        _list.append('')

    for string in S:
        string_len = len(string) - 1
        for idx in range(max_len):
            if string_len >= idx:
                _list[idx] = string[idx] + _list[idx]
            else:
                if _list[idx] == '':
                    pass
                else:
                    _list[idx] = '*' + _list[idx]

    for ans in _list:
        print(ans)
        
        
if __name__ == "__main__":
    main()
