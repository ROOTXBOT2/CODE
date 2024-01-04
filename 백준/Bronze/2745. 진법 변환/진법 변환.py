a, b = input().split(" ")

max_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 0
answer = 0

for i, num in enumerate(a[::-1]):
    answer += int(b) ** i * max_list.index(num)

print(answer)