from sys import stdin


def main():
    _input = stdin.readline
    N, M = map(int, _input().split(" "))
    a_line = list(map(int, _input().split(" ")))

    avg_x = int(M/N)
    _min = avg_x
    _max = 10 ** 10

    while _max - _min != 1:
        mid = (_min + _max) // 2
        if calc_sum_travel_costs(mid, a_line) > M:
            _max = mid
        else:
            _min = mid

    if _max == 10 ** 10:
        print("infinite")
    else:
        print(_min)


def calc_sum_travel_costs(_min:int, _list:list[int]) -> int:
    sum_costs = 0
    for i in _list:
        sum_costs += min(_min, i)
    return sum_costs



if __name__ == "__main__":
    main()
