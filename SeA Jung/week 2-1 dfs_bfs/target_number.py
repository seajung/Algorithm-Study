def dfs(numbers, depth, sum, target):
    if depth == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    return dfs(numbers, depth+1, sum + numbers[depth], target) + dfs(numbers, depth+1, sum - numbers[depth], target)
    

            
def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, 0, 0, target)
    return answer