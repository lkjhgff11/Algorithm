'''
# 문자열 팰린드롬인지 판단
word = list(input())
li = []
for w in range(len(word)-1,-1,-1):
    li.append(word[w])
  
if li == word:
    print(*li,sep='')
    print("입력하신 단어는 회문(Palindrome)입니다.")



# 단어 역순출력 ( A better tomorrow => tomorrow better A )
print(*reversed(input().split()))
#print(*reversed(input()),sep='') #  <- 방향으로 하나하나 역순 ( A better tomorrow => worromot retteb A )



address = input()
print("protocol: {}".format(address[:4]))
print("host: {}".format())
print("others: {}".format())


# 공백문자열 제거
data_str = "  홍  길동   "
data_str2 = data_str.lstrip(" ")
print("{}왼쪽공백 제거 : {}".format(data_str,data_str2))

data_str = "___홍  길동_________@@#$%"
data_str3 = data_str.rstrip("_@#$%")
print("{}오른쪽 _ 제거 : {}".format(data_str,data_str3))




# 문자열 자르기
data_str = "10,  20, 30,  40, 50"
data_str = data_str.replace(" ","")
print(data_str)

data_list = data_str.split(",")
for val in data_list:
    print(val)




# 문자열 구성 확인
data_str = "10,  20,  3o, 40,   50"

data_str = data_str.replace(" ","")
print(data_str)

data_list = data_str.split(",")
for val in data_list:
    print(val, end="")
    if not val.isdigit():
        print("<=", end="")
    print()    




# 문자열 찾기및 교체
data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."

mask_str = input("마스킹할 문자열을 입력하세요:")
find_str = input("찾을 문자열을 입력하세요:")
idx = -1
count = 1
while True:
    idx = data_str.find(find_str,idx+1)  # 찾고싶은문자 ,시작위치
    if idx != -1:
        print("[{0}] ~ [{1}]".format(idx,idx + len(find_str)-1))
        new_str = data_str.replace(find_str,mask_str,count)
        print(new_str)
        count += 1
    else:
        break



# 대문자변환
while True:
    string = input()
    if string == '':
        break
    print(string.upper())
    

# 사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고, 중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성

words = list(input().split())
words = set(words)
words = list(words)
words.sort()
print(*words,sep=',')


string = input()
ans = [string[x] for x in range(len(string)) if x%2 == 0]
print(*ans,sep='')



address = input()
one = address.split(':')
two = address.split('/')

print("protocol: {}".format(one[0]))
print("host: {}".format(two[2]))
print("others: {}".format(two[3]))


'''
import re
address = input()
p = re.compile('\\{}'.format(address))
print(p)
