import time
import random 
import matplotlib.pyplot as plt

# linear search algorithms
def linear_search (arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#binary search algorithms (requires sorted input)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:  
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test Linear Search
arr = [10, 30, 20, 40, 50]
target = 30
result = linear_search(arr, target)
print("linear Search Result:", result)

# Test Binary Search
arr = sorted([10, 20, 30, 40, 50])
target = 30
result = binary_search(arr, target)
print("binary Search Result:", result)

#Measure Algorithm Runtime
def measure_time(func, arr, target):
    start_time = time.perf_counter()
    func(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time

#Measure Algorithm Random number
arr = [random.randint(1, 100) for _ in range(1000)]
target = random.choice(arr)

#Measure runtime for linear Search 
linear_time = measure_time(linear_search, arr, target)
print("Linear Search Time:", linear_time)

#Measure runtime for binary Search (on sorted array)
sorted_arr = sorted(arr)
binary_time = measure_time(binary_search, sorted_arr, target)
print("Binary Search Time:", binary_time)

input_sizes = [100, 5000, 10000, 50000, 100000]
linear_times = []
binary_times = []

for size in input_sizes:
    arr = [random.randint(1, 100000) for _ in range(size)]
    target = random.choice(arr)
    sorted_arr = sorted(arr)

    #Measure times
    linear_times.append(measure_time(linear_search, arr, target))
    binary_times.append(measure_time(binary_search, sorted_arr, target))

print(linear_times)
print(binary_times)

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, linear_times, label="Linear Search", marker="o")
plt.plot(input_sizes, binary_times, label="Binary Search", marker="s")
plt.title("Runtime Comparison: Linear Search vs Binary Search")
plt.xlabel("Input Size (n)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.grid()
plt.show()