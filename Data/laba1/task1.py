import random
import time
import matplotlib.pyplot as plt

def foo(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a

sizes = [10, 50, 100, 200, 500, 1000]
times = []

for n in sizes:
    data = [random.randint(-100, 100) for _ in range(n)]
    start = time.perf_counter()
    foo(data.copy())
    times.append(time.perf_counter() - start)

plt.plot(sizes, times, 'o-')
plt.xlabel('n')
plt.ylabel('time (s)')
plt.grid(True)
plt.show()