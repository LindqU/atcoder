from sys import stdin


def main():
    N: int = int(stdin.readline().strip())
    As: list[int] = list(map(int, stdin.readline().strip().split(" ")))

    large_values:list[int] = []

    large_value: int = 0
    large_value_index : int = 0
    second_large_value: int = 0
    second_large_value_index : int = 0

    for idx, a in enumerate(As, 1):
        if a > large_value:
            second_large_value = large_value
            second_large_value_index = large_value_index
            large_value = a
            large_value_index = idx
        elif a > second_large_value:
            second_large_value = a
            second_large_value_index = idx
    
    print(second_large_value_index)


if __name__ == "__main__":
    main()
