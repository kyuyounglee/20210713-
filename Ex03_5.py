filename = "C:\\Program Files\\Adobe\\Adobe Creative Cloud\\test.txt"
# hint 문자열에서 디렉터리를 나타내는 방법은   /  로 표현하거나 \\

index1 = filename.rfind("\\")
print(index1)
index2 = filename.rfind(".")

name = filename[index1+1:index2]
ext = filename[index2+1:]
print( "파일명 = {}  확장자 = {}".format(name,ext) )
#화면에
# 파일명 :
# 확장자 :
