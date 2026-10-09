import time
import random
import matplotlib.pyplot as plt


def selection_sort(a):
    a = a[:]
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def quick_sort(a):
    a = a[:]

    def qs(lo, hi):
        if lo >= hi:
            return
        p = a[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while a[i] < p:
                i += 1
            while a[j] > p:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        qs(lo, j)
        qs(i, hi)

    qs(0, len(a) - 1)
    return a


def measure(f, data):
    t = time.perf_counter()
    f(data)
    return time.perf_counter() - t


def experiment():
    random.seed(0)
    sizes = [100, 200, 400, 800, 1600, 2000]
    variants = {"random": [], "sorted": [], "reversed": []}
    for n in sizes:
        base = list(range(n))
        variants["random"].append(random.sample(base, n))
        variants["sorted"].append(base[:])
        variants["reversed"].append(base[::-1])

    for name, arrays in variants.items():
        sel, qs = [], []
        for arr in arrays:
            sel.append(measure(selection_sort, arr))
            qs.append(measure(quick_sort, arr))
        plt.figure()
        plt.plot(sizes, sel, marker="o", label="selection sort")
        plt.plot(sizes, qs, marker="s", label="quick sort")
        plt.xlabel("N")
        plt.ylabel("time, s")
        plt.title(name)
        plt.legend()
        plt.grid(True)
        plt.savefig("plot_" + name + ".png", dpi=150)
        plt.close()


experiment()