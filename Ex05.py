import datetime

now= datetime.datetime.now();
month = now.month;
print(month)

# month 를 가지고 계절 판단하기
# 1  ~ 12

if month <= 2:
    print("겨울")   # 2 1 0 -1 -2 -3  ~~
elif month <= 5:
    print("봄")      #  3 4 5
elif month <= 8:
    print("여름")     # 6 7 8
elif month <= 11:
    print("가을")     # 9 10 11
else:
    print("겨울")     # 12


if "":
    print()
else:
    print()

