student = {
    'name' : "홍길동",
    'name' : "홍길동2",
    'addr' : '서울시',
    'subject' : {'kor' : 80, 'eng':98, 'math':88},
    'subject' : 100
}

for i in student:
    print(i," : ", student[i])

print("==================================================")

## 없는 키를 사용해서 값을 할당하면 Dictionary에 추가하는 형태
student["name2"] = "강감찬"
print(student)
student.pop('name2')
print(student)

#  1. Dictionary 두개 중에 한개라도 발견되면 true
#  2. Dictionary 두개다  발견되면 true

if ("name" in student) and ("addr" in student):
    print("찾았습니다.")
else:
    print("없습니다.")