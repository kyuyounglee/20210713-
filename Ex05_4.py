list_a = [1,2,3]
list_a.extend([4,5,6])
#list_a = list_a + [4,5,6]
#list_a.append([4,5,6])
print(list_a)

del list_a[0]
a = list_a.pop()
print(list_a,a)

list_a.insert(3,2)
print(list_a)
list_a.remove(2)
print(list_a)