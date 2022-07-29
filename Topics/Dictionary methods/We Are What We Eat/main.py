# the list "meals" is already defined
# your code here
calories = 0
for _ in meals:
    calories += _.get('kcal', 0)
print(calories)
