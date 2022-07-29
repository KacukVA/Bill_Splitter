num = int(input())
result = []
for _ in range(0, num):
    a = int(input())
    if a % 7 == 0 and a != 0:
        result.append(a)

for _ in result:
    print(_)
