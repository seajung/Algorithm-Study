def find_target(numbers, target):
    if not numbers:
        if (target == 0):
            return 1
        return 0
    next_list = numbers[1:]
    i = numbers[0]
    return  find_target(next_list, target-i) + find_target(next_list, target+i)

def solution(numbers, target):
    answer = find_target(numbers, target)
    return answer
