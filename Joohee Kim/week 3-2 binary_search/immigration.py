def solution(n, times):
    start = 1
    end = n * max(times)
    
    answer = end
    # binary search: O(logn)
    while start <= end: 
        mid = (start + end) // 2
        ppl = calc_ppl(mid, times)  # O(n)
        if ppl < n: # 시간 늘려야 함
            start = mid + 1
        else:   # 시간 줄여 볼 수 있음
            answer = min(mid, answer)
            end = mid - 1
    
    return answer


def calc_ppl(time, times):
    ppl = 0
    for t in times:
        ppl += time // t
    return ppl

# testcase
n = 6
times = [7, 10]
print(solution(n, times))   #28