# 1. 요소 5개를 갖는 임의의 리스를 만드세요
list_a = list(range(1,10,2) )
#2 1번에서 만든 리스트를 역으로 출력하는데. 두번 출력하세요
temp = list(reversed(list_a))
for i in reversed(list_a):
    print(i)
for i in reversed(list_a):
    print(i)
# 5
# 4
# 3
# 2
# 1
# 5
# 4
# 3
# 2
# 1

# 3. 1번의 리스트를 이용해서 enumerate 을 이용해서 인덱스와 값을 출력
for i,m in enumerate(list_a):
    print(i, m)
# 4. 3번을 이용해서 인덱스를 키로 하는 dictionary를 만드세요
dic_a = {}
for i,m in enumerate(list_a):
    dic_a[i] = m

# 5 4번에서 만든 dictionary를 .imtes()를 이용해서 key value를 for문으로 출력하세요
# 우리가 배운방식
for key,value in dic_a.items():
    print(key, value)
# 오리지널 방식
for key in dic_a:
    print(key, dic_a[key])


