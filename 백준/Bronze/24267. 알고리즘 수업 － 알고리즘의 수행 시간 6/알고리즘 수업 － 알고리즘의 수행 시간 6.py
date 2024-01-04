def calculate_operations(n):
    return (n * (n - 1) * (n - 2)) // 6

n = int(input())
operations = calculate_operations(n)

print(operations)
print(3)