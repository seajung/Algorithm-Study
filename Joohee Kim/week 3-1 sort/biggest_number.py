from functools import cmp_to_key
import numbers

def solution(numbers):
    answer = ''
    if numbers == [0]*len(numbers): # test 11
        return "0"
        
    num_str = [str(n) for n in numbers]
    # num_str.sort(key = cmp_to_key(lambda a,b: int(b+a) - int(a+b)))
    # num_str.sort(key = cmp_to_key(compare_str))
    num_str = quick_sort(num_str)
    for n in num_str:
        answer += n
    
    return answer


def compare_str(a, b):
    return int(b+a) - int(a+b)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left_arr, right_arr, mid_arr = [], [], []
    for num in arr:
        cmp = compare_str(num, pivot)
        if cmp < 0:
            left_arr.append(num)
        elif cmp > 0:
            right_arr.append(num)
        else:
            mid_arr.append(num)

    return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)

# testcase
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))    #9534330
