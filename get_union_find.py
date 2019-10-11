# 부모를 구한다.(예를들어 노드 1,2,3의 부모노드는 1,1,2일때 3은 2를 가리키고 2는1을가리킨다. 1은 1을 가리키니 2와 3은 모두 1이 부모노드)
def getParent(parent,x):
    if parent[x] == x:
        return x
    return getParent(parent,parent[x])

    
# 각 부모노드를 합친다.(작은쪽으로 합친다. 합친다 라는말은 연결하는거.)
def unionParent(parent,a,b):
    a = getParent(parent,a)  # a는 a의 부모노드 
    b = getParent(parent,b)  # b는 b의 부모노드

    if a < b:   # a가(b보다) 작을때
        parent[b] = a  # b의 부모노드는 a이다.

    else:       # b가(a보다) 작을때
        parent[a] = b  # a의 부모노드는 b이다.


# 같은 부모 노드를 가지는지 확인한다.
def findParent(parent,a,b):
    a = getParent(parent,a)
    b = getParent(parent,b)

    if a == b:  # 같은 부모를 가지면 연결되어있다.
        return 1

    else:
        return 0  # 연결이 안되어있다.

parent = [0]+[i for i in range(1,11)]
print(parent)

unionParent(parent,1,2)
unionParent(parent,2,3)
unionParent(parent,3,4)
unionParent(parent,5,6)
unionParent(parent,6,7)
unionParent(parent,7,8)
print("1과 5는 연결되어있나요?",findParent(parent,1,5))
print(parent)
unionParent(parent,1,5)
print("1과 5는 연결되어있나요?",findParent(parent,1,5))
print(parent)

    


