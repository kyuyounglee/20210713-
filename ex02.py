pi = 3.14
print(type(pi), pi)

pi2 = pi
pi2 = 100
print(type(pi2), pi2)

pi3 = pi2
pi3 = "안녕하세요"
print(type(pi3), pi3)

# 원의 넓이
pi = 3.1459265
r = 10
print("원의 넓이=",pi*r*r)
print("원의 넓이=",pi*(r**2))

string = "안녕하세요"
string += "1"
string *= 2
print(string)

num = 100
data = input("입력") # data 는 문자로 들어온다
print(data)
print(type(data)) # 확인해 봤더니  str   문자 맞네
print(num + float(data) )  #  숫자 + 문자  error  --> 숫자 + 숫자

# 키보드로부터 숫자를 입력받으면(정수 혹은 실수)  -> float으로 casting 하는게 안전하다



