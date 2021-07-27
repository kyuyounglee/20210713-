import keyword

str = "123456789"
print(str)
str1 = " hello "
print(str1+"world")
print(str1.lstrip()+"world")
print(str1.rstrip()+"world")
print(str1.strip()+"world")

str = """
그린컴퓨터
아카데미
"""

str2 = """
파이썬 수업
매주 월~목
"""

print(str+str2.strip())


print("abc10".isalnum())
print("abc".isalnum())
print("10".isalnum())

print("abc".isidentifier())
print(keyword.kwlist)
sevenup = 123
# 7up = 123

print("7up".isidentifier())
#False = 123

string = "!동해물과 동해를 연결해서 동해를"
print(string.find("동해"))  # 0
print(string.rfind("동해")) # 14
print("해" in string)

fileName = "ReadMe.test.txt"
fileName = "bugo.xlsx"

# 파일명과 확장자를 분리합시다..
# 파일 확장자 추출 하기 또는 파일명 추출하기
findIndex = fileName.rfind(".")
print( fileName[findIndex+1:] )
print( fileName[findIndex+1:len(fileName) ] )

# 파일명과 확장자를 분리해서 출력하세요

print(fileName[0 : findIndex]  )
print(fileName[: findIndex]  )