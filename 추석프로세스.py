def process(k):
    if k in dp:
        return dp[k]

    time = ncook_times[k]
    time += max([0] + [process(sub) for sub in arr[k]])

    dp[k] = time
    return time

def phase(k):
    if k in dp2:
        return dp2[k]
 
    p = set([k])
    if arr[k]:
        for sub in arr[k]:
            p |= phase(sub)
    dp2[k] = p 
    return p

        
# solution함수는 cook_times, odrder,k를 매개변수로 받아
# k단계 수행전 반드시 먼저 완료해야하는 단계개수, k단계를 완료하는데 걸리는 최소시간이 들은 배열을 반환한다.
def solution(cook_times,order,k):
    global ncook_times,arr,dp,dp2

    dp = {}
    dp2= {}
    arr = ['@']+[[]for _ in range(k+1)]
    ncook_times = ['@'] + cook_times
    summ = 0
    for a,b in order:
        arr[b].append(a)

    d = process(k)
    num = len(phase(k))-1
    return [d,num]

cook_times = [5, 30, 15, 30, 35, 20, 4]
order = [[2,4],[2,5],[3,4],[3,5],[1,6],[4,6],[5,6],[6,7]]  # order [a,b] : b 단계를 수행하기 위한 전단계 a
k = 6

print(solution(cook_times,order,k))
