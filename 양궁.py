# a,b,c,d,e

scores = [10,8,6,4,2,0]

def solution(target,positions):
    for i in range(1,len(target)):
        target[i] += target[i-1]
    print(target)

    summ = 0
    for y,x in position:
        user_score = (y**2 + x**2)**0.5

        for i,t in enumerate(target):
            if user_score <= t:
                summ += scores[i]
                break
            

    return summ
                
                    
target = [2,3,4,3,2]
position = [[0,0],[0,1],[1,1],[-3,5],[7,5],[10,0],[-15,22],[-6,-5],[3,3],[5,-5]]

print(solution(target,position))
