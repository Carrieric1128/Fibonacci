import sys

# Pure recursive method


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


# Determine the maximum value of n that causes a crash
n = 0
try:
    while True:
        fib_recursive(n+1)
        n += 1
except RecursionError:
    print("Maximum value of n for pure recursive method: ", n)
    print("Error message:", sys.exc_info()[1])

# Dynamic programming method


def fib_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
        return memo[n]


# Compute F(n+1) using dynamic programming
try:
    fib_dp(n+1)
    print("Dynamic programming method: F(n+1) =", fib_dp(n+1))
except RecursionError:
    print("Dynamic programming method: Error computing F(n+1) using dynamic programming.")
