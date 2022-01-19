def solution(citations):
    answer = 0
    #citations.sort()
    citations = quick_sort(citations)
    for i, num in enumerate(citations):
        h_number = len(citations) - i
        if num >= h_number:
            answer = h_number
            break

    return answer

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left_arr, right_arr, mid_arr = [], [], []
    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num > pivot:
            right_arr.append(num)
        else:
            mid_arr.append(num)

    return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)

citations = [3, 0, 6, 1, 5]
print(solution(citations))  #3