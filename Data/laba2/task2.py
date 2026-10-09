def tribonacci(n):
    # базовые случаи
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    # рекурсивный случай
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


for i in range(15):
    print(i, tribonacci(i))