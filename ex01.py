# Review  - 주석 -
import keyword


print("복습")   # 함수 - 명령의 단위 집합
# 리터럴
1.1
1
"복습"

#keywor - 예약어
print(keyword.kwlist)

#type 을 알려주는 함수
print(type(True))

print("안녕하세요"[2:4] )

# 정방향
print("안녕하세요"[4] )
# 역방향
print("안녕하세요"[-1] )

print("동해물과\n백두산이")
print(
"""\
동해물과
백두산이
"""
)

# 문자열의 길이
print(len("안녕하세요"))

print(3/2 - 3//2)

from random import *
print(randint(1,10))
print(randint(1,10))
print(randint(1,10))

str = "문자열"
print(type(str))
num = 123
# 타입이 다르면 에러는 발생한다. (다른언어는 강제 casting 을 해주지만..)
print(str+num)
