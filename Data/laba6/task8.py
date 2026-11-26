DENOMINATIONS = [1, 3, 4, 10, 50, 100]


def solve_limited_atm(amount, stock):
    coins = []
    for denom in DENOMINATIONS:
        max_needed = min(stock[denom], amount // denom)
        coins.extend([denom] * max_needed)

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    used_coins = [None] * (amount + 1)
    used_coins[0] = {d: 0 for d in DENOMINATIONS}

    for coin in coins:
        for s in range(amount, coin - 1, -1):
            if dp[s - coin] + 1 < dp[s]:
                dp[s] = dp[s - coin] + 1
                new_combo = used_coins[s - coin].copy()
                new_combo[coin] += 1
                used_coins[s] = new_combo

    return used_coins[amount]


if __name__ == "__main__":
    atm_stock = {}
    print("Введите начальное количество купюр/монет в банкомате:")
    for denom in DENOMINATIONS:
        atm_stock[denom] = int(input(f"Номинал {denom} руб.: "))

    clients_count = int(input("\nВведите количество клиентов: "))
    requests = []
    for i in range(1, clients_count + 1):
        req = int(input(f"Сумма для клиента №{i}: "))
        requests.append(req)

    print("\n--- Обслуживание клиентов ---")
    for i, amount in enumerate(requests, 1):
        print(f"\nКлиент №{i} запрашивает {amount} руб.:")
        result = solve_limited_atm(amount, atm_stock)

        if result is None:
            print("Невозможно выдать данную сумму из-за нехватки купюр и монет.")
        else:
            issued = {k: v for k, v in result.items() if v > 0}
            print("Выдано (номинал: количество):", issued)
            for denom, count in issued.items():
                atm_stock[denom] -= count
            print("Остаток в банкомате:", atm_stock)
