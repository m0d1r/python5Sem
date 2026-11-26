from itertools import combinations
import time
import random
import matplotlib.pyplot as plt


def knapsack_bruteforce(capacity, items):
    best_value = 0
    best_combination = []
    for r in range(1, len(items) + 1):
        for comb in combinations(items, r):
            total_weight = sum(item[1] for item in comb)
            total_value = sum(item[2] for item in comb)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = [item[0] for item in comb]
    return best_value, best_combination


def knapsack_greedy(capacity, items):
    sorted_items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    total_value = 0
    current_weight = 0
    chosen = []
    for name, weight, value in sorted_items:
        if current_weight + weight <= capacity:
            current_weight += weight
            total_value += value
            chosen.append(name)
    return total_value, chosen


def knapsack_dp(capacity, items):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    chosen = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, weight, _ = items[i - 1]
            chosen.append(name)
            w -= weight

    return dp[n][capacity], chosen[::-1]


def plot_benchmarks():
    sizes = [5, 8, 10, 12, 14, 16, 18]
    times_bf, times_greedy, times_dp = [], [], []
    capacity = 50

    for n in sizes:
        test_items = [(f"item_{i}", random.randint(1, 15), random.randint(10, 100)) for i in range(n)]

        start = time.perf_counter()
        knapsack_bruteforce(capacity, test_items)
        times_bf.append(time.perf_counter() - start)

        start = time.perf_counter()
        knapsack_greedy(capacity, test_items)
        times_greedy.append(time.perf_counter() - start)

        start = time.perf_counter()
        knapsack_dp(capacity, test_items)
        times_dp.append(time.perf_counter() - start)

    plt.plot(sizes, times_bf, label="Полный перебор O(2^n)", marker="o")
    plt.plot(sizes, times_greedy, label="Жадный алгоритм O(n log n)", marker="s")
    plt.plot(sizes, times_dp, label="Дин. программирование O(n*W)", marker="^")
    plt.xlabel("Количество предметов (n)")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Сравнение времени работы алгоритмов")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    cap = int(input("Вместимость рюкзака: "))
    count = int(input("Количество предметов: "))
    items_list = []
    for _ in range(count):
        name, weight, value = input("Название вес ценность: ").split()
        items_list.append((name, int(weight), int(value)))

    print("Полный перебор:", knapsack_bruteforce(cap, items_list))
    print("Жадный алгоритм:", knapsack_greedy(cap, items_list))
    print("Дин. программирование:", knapsack_dp(cap, items_list))

    plot_benchmarks()
