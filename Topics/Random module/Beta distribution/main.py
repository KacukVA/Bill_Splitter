import random
alpha = 0.9
beta = 0.1

random.seed(3)
# call the function here
result = random.betavariate(alpha, beta)
print(result)