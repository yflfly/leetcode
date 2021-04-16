def knapsack_1D_1(N, W, w, v):
    """ 0-1 背包 一维 dp """
    dp = [0] * (W + 1)
    for i in range(0, N):
        for j in range(W, -1, -1):  # [20,...,0]
            if w[i] <= j:
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    print("dp:\n", dp)
    print("dp[-1]:\n", dp[-1])


def a(N, W, w, v):
    w.insert(0, 0)
    v.insert(0, 0)
    dp = [[0 for j in range(W + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if j < w[i]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - w[i]] + v[i])
    return dp[-1][-1]


if __name__ == '__main__':
    N = 3  # 物品数量
    W = 10  # 背包容量
    # n = [2,1,2]
    w = [2, 5, 4]
    v = [3, 10, 12]
    knapsack_1D_1(N, W, w, v)
    print(a(N, W, w, v))
