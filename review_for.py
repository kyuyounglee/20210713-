for n in range(5):
    print(n)

list_a = [10,20,30,40]

for n in list_a:
    print(n)

person = {
    'name' : '홍길동',
    'age' : 20,
    'addr' : '서울시',
    'huby' : ['독서','잠자기','게임하기']
}
print(person['addr'])

for n in person:
    if type(person[n]) is list:
        for i in person[n]:
            print(n, ':', i)
    else:
        print(n," : ", person[n]  )


