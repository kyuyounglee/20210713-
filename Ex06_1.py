print(range(5))

for i in range(5):
    print(i)

print()

list_a = [2,4,2,5,9]

# if 문을 적절히 사용 할 것
for i in list_a:
    if i == 2:
        list_a.remove(2)

print(list_a)

# 리스트가 주어지고 그리고 삭제할 데이터가 주어지면
# 리스트에서 해당 값을 찾아서 전부 삭제 할것
