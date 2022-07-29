a = int(input())
b = int(input()) + 1
result = 0
count = 0
for i in range(a, b):
    if i == 0:
        count += 1
    elif int(i % 3) == 0:
        result += i
        count += 1

print(result / count)
