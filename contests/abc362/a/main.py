from sys import stdin


def main():
    R: int
    G: int
    B: int
    R, G, B = map(int, stdin.readline().split())

    C: str
    C = stdin.readline().strip()

    cost: int = 0

    if C == "Red":
        cost = min(G, B)
    elif C == "Green":
        cost = min(R, B)
    elif C == "Blue":
        cost = min(R, G)

    print(cost)


if __name__ == "__main__":
    main()
