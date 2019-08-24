'''
students = [(90,80),(85,75),(90,100)]

for i in range(len(students)):
    summ = sum(students[i])
    avg = summ/len(students[i])
    print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(i+1,summ,avg))
        

st = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
st2 = [s for s in st if s not in ('a','e','i','o','u')]

print(*st2,sep='')    


result= [] 
for i in range(2,10):
    r = []
    for j in range(1,10):
        if (i*j) % 3 != 0 and (i*j) % 7 !=0:
            r.append(i*j)
    result.append(r)

print(result)        

li = []
for _ in range(5):
    n = int(input())
    li.append(n)

summ = sum(li)
avg = summ/len(li)

print("입력된 값 {}의 평균은 {}입니다.".format(li,avg))

n = int(input())
s = []
for i in range(1,n+1):
    if n%i == 0:
        s.append(i)

print(s)
        

li = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
ans = [l for l in li if l%2 ==0]
print(ans)


def fibo(n):
    if n == 1:
        return 1
    if n == 2 :
        return 1

    return fibo(n-1)+fibo(n-2)
li = [fibo(i) for i in range(1,11)]
print(li)


print([x**2 for x in range(1,21) if x%3 !=0 or x%5 !=0 ])



nums = input()
summ = 0
for n in nums:
    summ += int(n)
print(summ)    



dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),

               ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
 

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',

                   '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',

                   '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']


inputWord.sort()
print(inputWord)



nums = tuple(map(int,input().split(',')))
li = list(nums)
print(li)
print(nums)

import math
pi = math.pi
r = list(map(int,input().split(',')))
r2 = []
for i in r:
     a = 2 * i * pi
     a = format(a,'.2f')
     r2.append(a)
print(*r2, sep = ', ')     
    


n,m = map(int,input().split(','))
li = []
for i in range(n):
    l = []
    for j in range(m):
        l.append(i*j)
    li.append(l)
print(li)


dic = list(input().split(','))
print(', '.join(sorted(dic)))

'''

nums = list(map(int,input().split(',')))
ans = [i for i in nums if i%2 != 0]
print(*ans,sep=', ')
            
