jumsu = int(input("점수를 입력하세요"))
hakjum = "F";
if jumsu >=90:
    hakjum = "A"
elif jumsu >=80:
    hakjum = "B"
elif jumsu >=70:
    hakjum = "C"
elif jumsu >=60:
    hakjum = "D"
else:
    hakjum = "F"
print("당신의 학점은: ",hakjum)

