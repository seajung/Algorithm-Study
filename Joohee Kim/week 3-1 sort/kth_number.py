def solution(array, commands):
    answer = []
    for ijk in commands:
        answer.append(cut_and_sort(array, ijk))
    return answer


def cut_and_sort(array, ijk):
    i, j, k = ijk[0], ijk[1], ijk[2]
    cut_array = array[i-1:j]
    #cut_array.sort()
    cut_array = quick_sort(cut_array)
    kth_num = cut_array[k-1]
    
    return kth_num


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

# testcase
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))    #[5,6,3]