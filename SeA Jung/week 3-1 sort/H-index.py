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


def solution(citations):
    answer = 0
    n = len(citations)
    quick_sort(citations,0,n-1)
    
    for i in range(n):
        if citations[i] >= n-i:
            answer = n-i
            break

    return answer