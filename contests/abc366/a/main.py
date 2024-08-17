from sys import stdin


def main():
    _input = stdin.readline
    N, T, A = map(int, _input().split(' '))
    
    # 有効投票数 N
    # 高橋氏 T
    # 青木氏 A
    if max(T, A) >= (N+1)/2:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
