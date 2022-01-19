def find(sub, k):
    sub.sort()
    return sub[k-1]

def solution(array, commands): # Sort 쓰는 경우
    L = len(commands)
    answer = []
    for [i, j, k] in commands:
        sub = array[(i-1):j]
        answer.append(find(sub, k))
    return answer
