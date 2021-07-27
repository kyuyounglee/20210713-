# 1 ~ 10 사이의 숫자 중에 짝수만 출력
for n in  range(1,11):
    if n % 2 == 0:
        print(n)

# 순환하는 도중에 뭔가를 제외 할때
for n in  range(1,11):
    if n % 2 != 0:
        continue;
    print(n)



key_list = ["name","hp","mp","level"]
value_list = ["기사",200,30,5]

character = {}
for index in range(4):
    key = key_list[index]
    value = value_list[index]
    character[key] = value

print(character)

