#문자형 정수를 변환할때는 int()
#문자형 실수를 변환할때는 float()
#문자형 숫자(실수 or 정수)  float()

data = 10.5
print("original data=",data)
print("remove point data =",int(data))
print(float(10))

# string -> int    "10"                 --> ok
# string -> int    "10.5"               --> error
# string -> float    "10"  or "10.5"    --ok
# print(int("10.5"))