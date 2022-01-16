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


def solution(array, commands):
    answer = []
    for i,j,k in commands:
        sliced_array = array[i-1:j]
        quick_sort(sliced_array,0,j-i)
        answer.append(sliced_array[k-1])
    return answer