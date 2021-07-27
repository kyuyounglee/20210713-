import random

list_a = [1,2,3,4,5]

# 리스트의 원소중에 2 와 3의 값을 변경
temp = list_a[1]
list_a[1] = list_a[2]
list_a[2] = temp

print( list_a)


# 1 ~ 45
rotto= list(range(1,46))
# random
print('섞기전 : ', rotto)

# 위치변경하기(두 변수의 값을 교환)
# 리스트의 첫번재 값과 임의의 위치에 해당하는 값을 교환

# for문이용하는 적당히 순환  대략 100번   rotto[0]
for i in range(1000):
    rnd = random.randrange(45)
    temp = rotto[0]
    rotto[0] = rotto[rnd]
    rotto[rnd] = temp

print('섞은후 : ', rotto)

# 번호 6개 뽑는거
# rotto[0] ~ rotto[5]
for i in range(6):
    print( rotto[i] )







