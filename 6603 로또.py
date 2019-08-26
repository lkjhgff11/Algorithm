from itertools import combinations
while True:
    nums = list(map(int,input().split()))
    if nums[0] == 0:
        break
    
    lotto = nums[1:]
    
    for x in combinations(lotto,6):
        print(*x)
    print()
