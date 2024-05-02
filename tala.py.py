import time

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

test_values = [5, 10, 20, 30, 40]

print("Testing Factorial Calculation Methods\n")
print("| n   | Iterative Result | Recursive Result |")
print("|-----|------------------|------------------|")
for n in test_values:
    start_time = time.perf_counter()
    result_iterative = factorial_iterative(n)
    iterative_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    result_recursive = factorial_recursive(n)
    recursive_time = time.perf_counter() - start_time

    print(f"| {n:3} | {result_iterative:16} | {result_recursive:16} |")
    print("|     | Iterative Time: {:.6f}s | Recursive Time: {:.6f}s |\n".format(iterative_time, recursive_time))
