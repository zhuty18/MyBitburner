a = 4
dp = [0] * (a + 1)


def NumberOfWays(n):
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
                dp[j] = dp[j] + dp[j - i]

    return dp[n] - 1


print(NumberOfWays(a))
