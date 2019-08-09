# { }로 딕셔너리 만들때는 {"키":값} 이런식으로 키는 " " 이걸로 문자열이어야함
data_dict1 = {"홍길동": 20, "이순신": 45, "강감찬": 35}
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))


# dict() 함수로 딕셔너리 만들때는 키값으로 문자열 하면안되고  dict(키 = 값) 이런 형식으로 해야함
data_dict2 = dict(홍길동 = 20, 이순신 = 45, 강감찬 = 35)
print("data_dict2: {} {}".format(type(data_dict2),data_dict2))

# (키,값)으로 구성된 튜플을 dict()함수써서 딕셔너리로 변환할수있음
data_tuple = (("홍길동",20),("이순신",45),("강감찬",35))
data_dict3 = dict(data_tuple)
print("data_dict3: {} {}".format(type(data_dict3),data_dict3))

# 리스트객체인데 (키,값)으로 구성된 튜플을 항목으로하는 리스트 객체를 dict함수로 딕셔너리 만들수있다.
data_list1 = [("홍길동",20),("이순신",45),("강감찬",35)]
data_dict4 = dict(data_list1)
print("data_dict4: {} {}".format(type(data_dict4),data_dict4))

# 셋 객체를 dict 함수를 사용해 딕셔너리 객체로 변환
data_set1 = {("홍길동",20),("이순신",45),("강감찬",35)}
data_dict5 = dict(data_set1)
print("data_dict5: {} {}".format(type(data_dict5),data_dict5))


# 딕셔너리 객체에 접근하는방법: 딕셔너리 객체이름["키값"]
data_dict1 = {"홍길동": 20, "이순신": 45, "강감찬": 35}
print("data_dict1['홍길동']=> {}".format( data_dict1["홍길동"] ))


# 딕셔너리 항목추가, 항목변경, 항목제거 ,항목확인, for문을 이용한 딕셔너리 항목 접근
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

# 딕셔너리 항목추가: 딕셔너리 객체이름["중복되지 않은 키"] = 값
data_dict1["을지문덕"] = 40
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))
data_dict1["뭉지"] = 32


# 딕셔너리 항목변경: 딕셔너리객체이름[중복되는키] = 값
data_dict1["뭉뭉"] = 1
data_dict1["헝헝"] = 60
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))



# 2개이상의 항목을 변경할때는 update함수로  여러개 항목추가및 변경 가능  딕셔너리 객체이름.update({"밍밍": 20, "뭉뭉":30})
data_dict1.update({"뭉뭉": 20, "홍홍": 21, "헝헝": 26})
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))


data_dict1.update({"홍길동": 900, "이순신": 800, "뭉지":2100})
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

# 삭제 명령어 del: del 객체이름["키"]
del data_dict1["강감찬"] 
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

# pop 함수를 호출해서 데이터 삭제 가능
data_dict1.pop("홍길동")
print("data_dict1: {} {}".format(type(data_dict1),data_dict1))

print()
# clear()은 모든항목이 삭제되고, {} 빈 딕셔너리 객체 리터럴을 출력
data_dict1.clear()
print("data_dict1: {} {}".format(type(data_dict1),data_dict1))

data_dict1 = {"홍길동": 20, "이순신": 45, "강감찬": 35}
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

print("'홍길동' in data_dict1 => {}".format("홍길동" in data_dict1))
print("'신사임당' not in data_dict1 => {}".format("신사임당"not in data_dict1))
print("'홍길동' not in data_dict1 => {}".format("홍길동" not in data_dict1))

# data_dict1.items()는 (키,값) 튜플들, keys는 key들(문자열로 구성), values는 값들(정수로 구성)..
print("data_dict1 items: {} {}".format(type(data_dict1.items()),data_dict1.items()))
print("data_dict1 keys: {} {}".format(type(data_dict1.keys()),data_dict1.keys()))
print("data_dict1 values: {} {}".format(type(data_dict1.values()),data_dict1.values()))

# 각 항목의 키는 변소 key에 저장되며, data_dict1[key]로 해당키에 대응하는 값을 읽음
for key in data_dict1:
    print("key, data_dict1[key] => '{}','{}'".format(key,data_dict1[key]))

print()

# 매 반복에서 각 항목의 키가 변수 key에 저장되고, data_dict1[key]로 해당 키에 대응하는 값을 읽음
for key in data_dict1.keys():
    print("key,data_dict1[key] => '{}','{}'".format(key,data_dict1[key]))

# 튜플을 값으로 받아오는데 각 항목이 변수 item에 저장됙 item[0]: 키, item[1]: 값을 읽어옴.
for item in data_dict1.items():
    print("item[0] item[1] => '{}','{}'".format(item[0],item[1]))

# 위의 경우를 좀더 쉽게 튜플을 변수 각각 key,value로 받아오면 좀더 편함.
for key,value in data_dict1.items():
    print("key,value = > '{}',{}".format(key,value))  # 매 반복에서 각 항목의 키,값이 변수 key,value에 저장되어 읽음

# values()를 사용해서 돌면 매 반복에서 각 항목의 값이 변수 value에 저장되어읽어옴.    
for value in data_dict1.values():
    print("vlaue=> {}".format(value))     # 매 반복에서 각 항목의 값이 변수 value에 저장되어 읽어옴.

data_dict1.clear()
# 딕셔너리 내포를 이용해 딕셔너리 생성   
data_dict1 = {"홍길동": 20, "이순신": 45, "강감찬": 35}
data_set1 = {item for item in data_dict1.items()}  # 반복가능한 자료형의 경우 for문으로 내포기능사용
print("key, data_dict1[key] => '{}','{}'".format(key,data_dict1[key]))
print("data_set1 = {} {}".format(type(data_set1),data_set1)) # data_dict1과 동일한 기능을하는 data_set1이 만들어짐.

# 딕셔너리 내포기능으로 data_dict1의 항목을 가진 data_dict2 딕셔너리 객체 생성
data_dict2 = {key: data_dict1[key] for key in data_dict1}
print("data_dict2: {} {}".format(type(data_dict2),data_dict2)) 

print()
# data_dict1.keys()함수 호출에 의해 반환된 dict_keys 객체의 항목을 가진 data_dict3 딕셔너리객체 생성
data_dict3 = {key: data_dict1[key] for key in data_dict1.keys()}
print("data_dict3: {} {}".format(type(data_dict3),data_dict3)) 

# dict_items 객체의 튜플 객체 항목을 각각 변수 key, value에 저장하고, key,value 형식의 쌍을 항목으로가진 data_dict5 딕셔너리 객체 생성
data_dict4 = {key:value for key,value in data_dict1.items()}
print("data_dict4: {} {}".format(type(data_dict4),data_dict4)) 
