import time
import matplotlib.pyplot as plt


def fib_recursive(n):
    if n <= 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_dynamic(n):
    fib = [0] * (n+1)
    fib[1] = 1
    fib[2] = 1
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


def measure_execution_time(function, n):
    start_time = time.time()
    function(n)
    end_time = time.time()
    return end_time - start_time


n_values = list(range(10, 101, 10))
recursive_times = []
dynamic_times = []

# Maximum execution time for recursive method (adjust as needed)
max_recursive_time = 1000000

for n in n_values:
    print("n = ", n)
    if n >= 50:
        recursive_time = max_recursive_time
        print("Pure Recursive: {:.10f} sec".format(recursive_time))
    else:
        recursive_time = measure_execution_time(fib_recursive, n)
        print("Pure Recursive: {:.10f} sec".format(recursive_time))
    dynamic_time = measure_execution_time(fib_dynamic, n)
    print("Dynamic Programming: {:.10f} sec".format(dynamic_time))
    recursive_times.append(recursive_time)
    dynamic_times.append(dynamic_time)

plt.plot(n_values, recursive_times, label='Recursive')
plt.plot(n_values, dynamic_times, label='Dynamic Programming')
plt.xlabel('Value of n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of F(n) for Different Methods')
plt.legend()
plt.show()
