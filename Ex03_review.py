# 문자열 format - 다양한 문자열
# 0동 0호의 이번달 요금은 000 입니다.

string =  "{}동 {}호의 이번달 요금은 {} 입니다.".format(101,101,25000)
print(string)

age = 100;
print(type(age))    #  int
age = 10.5
print(type(age))    #  float
age = "열한살"
print(type(age))    # str

# 변수의 타입을 변환 -- cast   type casting
# 숫자형문자 -> 숫자   숫자 -> 숫자형문자

print(int("123"))
print(float("123"))

print(str(123))
print(type(str(123)))

num =  input("숫자를입력하세요")   # 123
print(type(num))
#num = int(num);
#num += 50


#print(num + 2)
print(num * 2)

print(5/2)
print(5//2)
print(5%2)
