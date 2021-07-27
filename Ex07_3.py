# 임의의 번호 6개 생성하기  1 ~ 45  그리고 리스트에 담기
# 결론 1 ~45사이의 숫자 6개로 이루어진 리스트를 만들어 보세요
import random
list_a = []
for i in range(10):
    for i in range(6):
        temp = random.randrange(1, 46)
        list_a.append(temp)
    print(list_a)
    list_a.clear()


