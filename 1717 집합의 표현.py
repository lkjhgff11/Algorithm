# 합집합 : 0,a,b
# a,b가 같은 집합에 포함되어있는지 확인한다: 1,a,b

parent = [0]*1000001

def Find(x):
    if x == parent[x]:
        return x

    else:
        y = Find(parent[x])
        parent[x] = y
        return y


def Union(x,y):
    x = Find(x)
    y = Find(y)
    parent[y] = x



n,m = map(int,input().split())
for i in range(n+1):
    parent[i] = i
    
    
for _ in range(m):
    op,a,b = map(int,input().split())

    if op == 0:
        Union(a,b)

    elif op == 1:
        a_parent = Find(a)
        b_parent = Find(b)

        if a_parent == b_parent:
            print("YES")

        else:
            print("NO")
