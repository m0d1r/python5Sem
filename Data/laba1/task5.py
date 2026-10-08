import time
import matplotlib.pyplot as plt

def measure_list_in(n):
    lst = list(range(n))
    target = n + 1
    start = time.perf_counter()
    for _ in range(1000):
        _ = target in lst
    return (time.perf_counter() - start) / 1000

def measure_set_in(n):
    s = set(range(n))
    target = n + 1
    start = time.perf_counter()
    for _ in range(1000):
        _ = target in s
    return (time.perf_counter() - start) / 1000

sizes = [500, 1000, 2000, 4000, 8000]
list_times = []
set_times = []

for n in sizes:
    list_times.append(measure_list_in(n))
    set_times.append(measure_set_in(n))

plt.figure(figsize=(10, 6))
plt.plot(sizes, list_times, marker='o', label='list', color='red')
plt.plot(sizes, set_times, marker='s', label='set', color='blue')

plt.xlabel('N')
plt.ylabel('Время')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()