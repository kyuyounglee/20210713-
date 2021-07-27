list_a = [10,20,30,40]
print(list_a)

# 1 reversed  순수하게 reversed를 사용하면 된다
for n in reversed(list_a):
    pass
# 2. reversed 를 한 후에 다시 리스트에 담아서 사용하면 된다.
list_a_rev = list(reversed(list_a))
for n in list_a_rev:
    pass
# 3 reversed를 변수에 담아서 사용하면 처음은 가능하지만 위치정보가 초기화 안되서 두번째 부터 안됨
# 처음한번은 되지만 두번째 부터는 출력안됨
temp = reversed(list_a)
for n in temp:
    pass

