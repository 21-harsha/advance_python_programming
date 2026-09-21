def bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


def top_down(values, weights, W, n, memo):
    if n == 0 or W == 0:
        return 0

    if (n, W) in memo:
        return memo[(n, W)]

    if weights[n - 1] > W:
        ans = top_down(values, weights, W, n - 1, memo)
    else:
        ans = max(
            values[n - 1] + top_down(values, weights, W - weights[n - 1], n - 1, memo),
            top_down(values, weights, W, n - 1, memo)
        )

    memo[(n, W)] = ans
    return ans


# Input from user
n = int(input("Enter number of items: "))

values = list(map(int, input("Enter values: ").split()))
weights = list(map(int, input("Enter weights: ").split()))

W = int(input("Enter capacity: "))

print("Bottom-Up:", bottom_up(values, weights, W))

memo = {}
print("Top-Down:", top_down(values, weights, W, n, memo))
