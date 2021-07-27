name = ["홍길동","이순신","강감찬","유관순"]
age = [50,30,40,25]
addr = ["서울시","경기도","충청도","부산"]

# 이름에서 찾고자 하는 이름의 해당 인덱스를 반환
try:
    findname = input("찾는사람 이름을 입력하세요")
    index = name.index(findname)
    print("찾았습니다.")
    print(name[index],age[index],addr[index])
except ValueError as e:
    print(e)
    print("찾고하는 사람이 없습니다.")




