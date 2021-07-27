list_a = ["안녕","하세","요"]
index = 0
for i in list_a:
    print("{}번째의 list_a는 {} 입니다.".format(index, i))
    index += 1

# enumerate 를 사용하면. ..... 기존 리스를 dictionary 구조로 변경
# enumerate(list_a)
# 0 : "안녕"
# 1 : "하세"
# 2 : "요"

for key,value in enumerate(list_a):
    print(key," : ", value)
