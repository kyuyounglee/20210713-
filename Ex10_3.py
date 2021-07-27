# 임의의 리스를 만들어 봅시다
list_a = [10,20,50,40,30]
for i in list_a:
    pass

reversed(list_a)  # 기존 리스를 뒤집어서 다시 리스트 X
for i in reversed(list_a):
    pass

revList = list(reversed(list_a))
for i in revList:
    pass

### 사용하면 안되는 형식  1번은 되나 2번이상 사용 x
temp = reversed(list_a)
for i in temp:
    pass

list_a = [10,20, 40,5,35]
# 리스트중에서 가장 큰 값을 갖는 인덱스의 위치를 찾아라
max = list_a[0]
findindex = 0;
for index,value in enumerate(list_a):
    if(max < value):
        max = value
        findindex = index
print("max = ", max)
print("index = ", findindex)




dic_test = {
    1 : "일",
    2 : "이",
    3 : "삼"
}

for key in dic_test:
    print(key, " : ", dic_test[key])

for key,value in dic_test.items():
    print(key," : ", value)


# reversed(리스트)   자체를 for문으로 사용하거나. list로 만들어서 사용한다.
# enumerate  리스트를 key : value 형식으로 만들어준다... 이때 key는 인덱스가 된다.(0 1 2 3~~)
# dictionary 형태의 변수에 .items()  --> enumerate 형태로 변경된다, for문을 사용할때 key: value 형태로사용


list_a = [10,21,30,41]
print(list_a)

list_b =  [n+5 for n in list_a]
print(list_b)

list_b =  [n+5 for n in list_a if n % 2 == 0]
print(list_b)
