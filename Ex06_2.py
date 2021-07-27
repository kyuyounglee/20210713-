list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
    ]


for i in list_of_list:
    for data in i:
        pass
        # print(data)


# 구구단....... 4 단

#  9번
for dan in range(2,10):  # 2 ~ 9
    for i in range(1,10): # 1 ~ 9
        print(dan," x ", i, " = ", dan * i)
    print()

name = '이름'
dic_key = {
    'name' : "7D 망고",
    type : "당절임"
}
print(dic_key['name'])

