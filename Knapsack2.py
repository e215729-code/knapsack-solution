n = 18
capacity = 45
size  = [ 4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
price = [ 6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]


import time

def unbounded_knapsack_dp(capacity, size, price):
    n = len(size)
    dp = [0] * (capacity + 1)

    start_time = time.time()

    for c in range(capacity + 1):
        for i in range(n):
            if size[I] <= c:
                dp[c] = max(dp[c], price[I] + dp[c - size[I]])

    end_time = time.time()

    execution_time = end_time - start_time

    return dp[capacity], execution_time

max_price, exec_time = unbounded_knapsack_dp(capacity, size, price)
print(f"ナップサックの最大価値: {max_price}”)
print(f"実行時間: {exec_time:.6f} 秒")