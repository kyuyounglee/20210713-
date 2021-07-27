# 리스트
list_a = [10, 20, 30]
# 리스트의 각 요소에 접근하기
list_a[0]  # 10  -> index 방식   index 라고 하면 0부터시작 숫자

# for 문을 이용
for i in list_a:    # 리스트를 순환하면 각각의 요소의 값을 i 변수에 저장
    print(i)        # 10 20 30 이렇게 순차적으로 리스트의 값을 가져옮

# for 문중에 range를 이용
for i in range(3):  # range(3)  0 1 2  즉 여기서는 i 가 index
    print(list_a[i])

