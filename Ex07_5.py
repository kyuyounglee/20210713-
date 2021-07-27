# dictionary
# 특징 : key : value 가 하나의 쌍으로 이루어진 집합
# key : value  --> 하나의 요소
di = {
    "name" : "기사",
    "level" : 12
}
# 각 요소에 접근할때는 index 방식이 아니라. key 방식  ["name"]
# print( di["name"] )

# for문 :   key 값을 반환한다
for i in di:
    print(i," : ", di[i])