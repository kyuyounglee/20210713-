# 숫자 맞추기 게임
# 규칙... 0 ~ 100 사이의 임의 숫자를 컴퓨터가 선택
# 사용자가 맞추는 게임
# ex  컴퓨터가 10   사용작 20 입력하면..... 크다
# ex  컴퓨터가 10   사용작 5 입력하면..... 작다
# 사용하는 순환문은  while true:
# 순환문 안에서 사용자의 입력값과 비교해서  크다 작다를 출력하고
# 맞추면 순환문을 종료   break 사용
# userNumber =  int(input("숫자를 입력하세요")
# compNumber = random.randrange(100) -- 순환문 밖에서 한번 정함
import random

compNumber = random.randrange(100)
while True:
    userNumber = int(input("숫자를 입력하세요"))
    if compNumber < userNumber:
        print("사용자의 값이 크다")
    elif compNumber > userNumber:
        print("사용자의 값이 작다")
    else:
        print("짝짝짝..!!!")
        break