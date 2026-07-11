n = 18
capacity = 45
size  = [ 4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
price = [ 6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]



def unbounded_knapsack_dp(capacity, size, price):
    n = len(size)
    dp = [0] * (capacity + 1)

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[capacity], execution_time

max_price, exec_time = unbounded_knapsack_dp(capacity, size, price)
print(f"ナップサックの最大価値: {max_price}”)