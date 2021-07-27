import random

sum = 0
while True:
    number = random.randrange(1, 100)
    sum = sum + number;
    if sum > 100:
        break

print(sum)