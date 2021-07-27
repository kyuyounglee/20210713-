# 로또 중복제거
import math
import random
list_a = []
count = 0
#for i in range(100):
while True:
    count = count + 1
    number = random.randrange(1,46)
    if number not in list_a:
        list_a.append(number)
    if len(list_a) == 10:
        break


print(count, " : ",list_a)