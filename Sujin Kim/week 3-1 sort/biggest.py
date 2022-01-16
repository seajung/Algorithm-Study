def merge_sort(arr):
    
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if (low_arr[l]*3 > high_arr[h]*3):
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def solution(numbers):
    answer = ''
    sub = []
    numbers = list(map(str, numbers))
    sort_numbers = merge_sort(numbers)
    answer = str(int(''.join(sort_numbers))) # test 11 [0, 0, 0, 0]->[0000] 실제론 0이 출력되어야함 
    return answer
