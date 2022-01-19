def solution(numbers):
    answer = ''
    sub = []
    numbers = list(map(str, numbers))
    sub.append(numbers[0])
    for i in range(len(numbers)):
        for j in range(i):
            if(sub[j]*3 < numbers[i]*3):
                sub.insert(j, numbers[i]) # O(N)
                break
        if(len(sub) == i):
            sub.append(numbers[i])
    answer = ''.join(sub)
    return answer
  
  ## 시간 초과로 몇 문제 실패
