# 문제..
# 두 개의 수를 입력 받아서
# 나누기를 해서
# 소수점 둘재 자리까지 출력 반올림
# a / b    12.567    12.564
#           12.57       12.56


data = 12.568
print("{:.2f}".format(data))

data *= 100
data = int(data)
data /= 100
print("{:.2f}".format(data))