import time
import matplotlib.pyplot as plt

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def fib_with_lucas(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    i = n // 2
    j = n - i
    fi = fib_with_lucas(i)
    li = lucas_with_fib(i)
    fj = fib_with_lucas(j)
    lj = lucas_with_fib(j)
    return (fi + lj)* (fj + li) // 2


def lucas_with_fib(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return fib_with_lucas(n - 1) + fib_with_lucas(n + 1)

ns_naive = list(range(20, 36, 2))
t_naive = []
for n in ns_naive:
    t0 = time.perf_counter()
    fibonacci(n)
    t_naive.append(time.perf_counter() - t0)

ns_fast = list(range(20, 201, 20))
t_fast = []
for n in ns_fast:
    t0 = time.perf_counter()
    fib_with_lucas(n)
    t_fast.append(time.perf_counter() - t0)

plt.figure()
plt.plot(ns_naive, t_naive, marker="o", label="fibonacci")
plt.plot(ns_fast, t_fast, marker="s", label="fib_with_lucas")
plt.xlabel("n")
plt.ylabel("time, s")
plt.legend()
plt.grid(True)
plt.savefig("plot_fib.png", dpi=150)
plt.close()