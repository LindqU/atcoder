from sys import stdin
from enum import Enum

def main(): 
    n = int(input())
    s = input()

    dp = [[-1 for _ in range(3)] for _ in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = 0
    dp[0][2] = 0
    for i in range(n):
        if s[i] == 'R':
            dp[i + 1][0] = max(dp[i][1], dp[i][2])
            dp[i + 1][1] = max(dp[i][0] + 1, dp[i][2] + 1)
        elif s[i] == 'P':
            dp[i + 1][1] = max(dp[i][2], dp[i][0])
            dp[i + 1][2] = max(dp[i][0] + 1, dp[i][1] + 1)
        elif s[i] == 'S':
            dp[i + 1][0] = max(dp[i][1] + 1, dp[i][2] + 1)
            dp[i + 1][2] = max(dp[i][0], dp[i][1])

    print(max(dp[n][0], dp[n][1], dp[n][2]))


if __name__ == "__main__":
    main()