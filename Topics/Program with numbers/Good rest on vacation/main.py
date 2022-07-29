duration = abs(int(input()))
food_cost = abs(int(input()))
fly_cost = abs(int(input())) * 2
hotel_cost = abs(int(input()))
print(food_cost * duration + hotel_cost * (duration - 1) + fly_cost)
