def find(arr, k): # using quick sort
    if len(arr) <= 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    
    lesser_arr, equal_arr, greater_arr = [], [], []
    
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
            
    if(len(lesser_arr)==(k-1)):
        return equal_arr[0]
    elif(len(lesser_arr)>(k-1)):
        return find(lesser_arr, k)
    elif(len(greater_arr)>len(arr)-k):
        return find(greater_arr, k-len(lesser_arr)-len(equal_arr))
    else:
        return equal_arr[0]
                    
def solution(array, commands): # Sort 쓰는 경우
    L = len(commands)
    answer = []
    for [i, j, s] in commands:
        sub = array[(i-1):j]
        answer.append(find(sub, s))
        print(answer)
    return answer
