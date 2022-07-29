walks = [
    {"day": "Monday", "distance": 2000},
    {"day": "Tuesday", "distance": 3000},
    {"day": "Wednesday", "distance": 3500},
    {"day": "Thursday", "distance": 2500},
    {"day": "Friday", "distance": 2500},
    {"day": "Saturday", "distance": 1000},
    {"day": "Sunday", "distance": 5600}]

# the list "walks" is already defined
# your code here
a = 0
b = 0
for _ in walks:
    a += _.get('distance')
    b += 1
print(a / b)
