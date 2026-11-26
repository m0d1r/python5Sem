def longest_common_substring(word_a, word_b):
    m, n = len(word_a), len(word_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word_a[i - 1] == word_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
            else:
                dp[i][j] = 0
    return max_len


if __name__ == "__main__":
    typo_word = input("Введите слово с ошибкой: ").strip().lower()
    candidates = input("Введите список похожих слов через пробел: ").strip().lower().split()

    best_word = max(candidates, key=lambda w: longest_common_substring(typo_word, w))
    print("Самое похожее слово (по общей подстроке):", best_word)
    