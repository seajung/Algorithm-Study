def quick_sort(array, start, end):
    if start >= end: 
        return
    
    pivot = start 
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            #swap
            array[right], array[pivot] = array[pivot], array[right]
        else: 
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

def solution(numbers):
    answer = ''
    str_nums=[]

    for num in numbers:
        str_nums.append(str(num))

    '''        
    str_nums.sort(key=lambda x: x * 3, reverse=True)
        
    for num in str_nums:
        answer += num
    '''
    quick_sort(str_nums,0,len(str_nums)-1)
    
    for i in range(len(str_nums)-1):
        if str_nums[i]*3 > str_nums[i+1]*3:
            str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
    
    str_nums.reverse()
    
    for num in str_nums:
        answer += num

    # 예외 처리
    if int(answer) == 0:
        answer = "0"
    return answer