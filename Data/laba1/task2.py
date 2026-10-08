import random
import time
import matplotlib.pyplot as plt

def min_max_linear(arr):
    if not arr:
        return None, None
    mn = mx = arr[0]
    for x in arr[1:]:
        if x < mn:
            mn = x
        elif x > mx:
            mx = x
    return mn, mx

def min_max_sort(arr):
    if not arr:
        return None, None
    sorted_arr = sorted(arr)
    return sorted_arr[0], sorted_arr[-1]

sizes = [10, 100, 500, 1000, 2000, 3000, 5000, 10000]
times_linear = []
times_sort = []

for n in sizes:
    data = [random.randint(-1000, 1000) for _ in range(n)]
    
    start = time.perf_counter()
    min_max_linear(data)
    times_linear.append(time.perf_counter() - start)
    
    start = time.perf_counter()
    min_max_sort(data)
    times_sort.append(time.perf_counter() - start)

plt.plot(sizes, times_linear, 'o-', label='Linear O(n)')
plt.plot(sizes, times_sort, 's-', label='Sorting O(n log n)')
plt.xlabel('n')
plt.ylabel('time (s)')
plt.legend()
plt.grid(True)
plt.show()