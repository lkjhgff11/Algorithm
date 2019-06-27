nanjang=[int(input()) for i in range(9)] 
#nanjang=sorted(nanjang) 
nanjang.sort() 
 
result = False 
# 몇번 돌았는지 index , nums 
def rec(index,nums): 
    if result: 
        return 
    if index==9: 
        if len(nums) == 7 and sum(nums) == 100: 
            result = True 
            print(*nums,sep="\n") 
        return 
 
    rec(index+1, nums) 
    nums.append(nanjang[index]) 
    rec(index+1,nums) 
    nums.pop() 
 
 
 
rec(0,[]) 
