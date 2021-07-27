# 랜덤하게 숫자 생성하기
import random

list_a = []
for i in range(20):
    list_a.append( random.randint(1,10) )
# 리스트 만든거 확인
print(list_a)
# 숫자가 몇번 나왔는지 확인용 dictionary
counter = {}

for i in list_a:
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] = counter[i] + 1

print(counter)

