import time
import matplotlib.pyplot as plt

def measure_list_del(n):
    lst = list(range(n))
    start = time.perf_counter()
    for _ in range(n):
        del lst[0]
    return time.perf_counter() - start

def measure_dict_del(n):
    d = {i: i for i in range(n)}
    start = time.perf_counter()
    for key in range(n):
        del d[key]
    return time.perf_counter() - start

sizes = [500, 1000, 2000, 4000, 8000]
list_times = []
dict_times = []

for n in sizes:
    list_times.append(measure_list_del(n))
    dict_times.append(measure_dict_del(n))

plt.figure(figsize=(10, 6))
plt.plot(sizes, list_times, marker='o', label='list', color='red')
plt.plot(sizes, dict_times, marker='s', label='dict', color='blue')

plt.xlabel('N')
plt.ylabel('Время')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()