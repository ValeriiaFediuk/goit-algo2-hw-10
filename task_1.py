import random
import time
import matplotlib.pyplot as plt
import numpy as np

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    return time.time() - start_time

sizes = [10000, 50000, 100000, 500000]
randomized_times = []
deterministic_times = []

for size in sizes:
    arr = [random.randint(0, 1000000) for _ in range(size)]
    
    rand_time = np.mean([measure_time(randomized_quick_sort, arr) for _ in range(5)])
    det_time = np.mean([measure_time(deterministic_quick_sort, arr) for _ in range(5)])
    
    randomized_times.append(rand_time)
    deterministic_times.append(det_time)
    
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, label='Рандомізований QuickSort', marker='o')
plt.plot(sizes, deterministic_times, label='Детермінований QuickSort', marker='s')
plt.xlabel('Розмір масиву')
plt.ylabel('Час виконання (секунди)')
plt.title('Порівняння часу виконання QuickSort')
plt.legend()
plt.grid()
plt.show()
