DENOMINATIONS = [1, 3, 4, 10, 50, 100]


def atm_greedy(amount, coins):
    result = []
    remaining = amount
    for coin in sorted(coins, reverse=True):
        while remaining >= coin:
            remaining -= coin
            result.append(coin)
    return result


def atm_dp(amount, coins):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    result = []
    curr = amount
    while curr > 0:
        coin = parent[curr]
        result.append(coin)
        curr -= coin
    return sorted(result, reverse=True)


if __name__ == "__main__":
    n = int(input("Введите сумму для снятия: "))

    greedy_res = atm_greedy(n, DENOMINATIONS)
    dp_res = atm_dp(n, DENOMINATIONS)

    print(f"Жадный алгоритм ({len(greedy_res)} шт.): {greedy_res}")
    print(f"Дин. программирование ({len(dp_res)} шт.): {dp_res}")
