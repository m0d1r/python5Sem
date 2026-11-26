def longest_common_subsequence(word_a, word_b):
    m, n = len(word_a), len(word_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word_a[i - 1] == word_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


if __name__ == "__main__":
    typo_word = input("Введите слово с ошибкой: ").strip().lower()
    candidates = input("Введите список похожих слов через пробел: ").strip().lower().split()

    best_word = max(candidates, key=lambda w: longest_common_subsequence(typo_word, w))
    print("Самое похожее слово (по общей подпоследовательности):", best_word)
