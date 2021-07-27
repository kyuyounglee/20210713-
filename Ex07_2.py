character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

d = character["items"]
for i in d:
    print(d[i])

li = character["skill"]
for i in li:
    print(i)




# 1 key : value 형식으로 일단 출력
for key in character:
    if type(character[key]) is dict:
        d = character[key]
        for key2 in d:
            print(key2, " : ", d[key2])
    elif type(character[key]) is list:
        d = character[key]
        for key2 in d:
            print(key, " : ", key2)
    else:
        print(key, " : ", character[key])


