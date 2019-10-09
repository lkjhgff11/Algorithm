# Merge Sort: O(nlogn)으로 빠름
# n/2로 나누고, 1개씩의 요소가 남기까지 재귀적으로 conquer한다.
# 그다음에 2개씩의 요소들을 반복적으로 merge한다.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left1 = merge_sort(left)   # 재귀를 이용하여 나눠진 왼쪽 부분을 다시 반으로 나눈다.
    right1 = merge_sort(right)

    return merge(left1,right1)
     

def merge(left,right):
    i = 0
    j = 0
    sorted_list = []

    while (i<len(left)) & (j<len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while (i<len(left)):
        sorted_list.append(left[i])
        i += 1

    while (j<len(right)):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


arr = list(map(int,input().split()))
print(merge_sort(arr))
