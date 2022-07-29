a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
door = x * y
if a * b <= door or a * c  <= door or b * c <= door:
    print('The box can be carried')
else:
    print("The box cannot be carried")
