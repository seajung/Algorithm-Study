def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()    #O(nlogn)
    rocks.append(distance)
    start = 1
    end = distance
    # binary search: O(logn) --> total: O(nlogn)
    while start <= end:
        mid = (start + end) // 2    # 목표하는 최소값이라고 가정
        prev = 0
        remove_cnt = 0
        dist_min = distance
        
        for rock in rocks:  # O(n)
            btw_rock = rock - prev
            # 목표 최소값보다 작으면, 늘리기 위해 돌 파괴 (prev 업데이트x)
            if btw_rock < mid:
                remove_cnt += 1
            # 그렇지 않으면, 돌 파괴x
            else:
                dist_min = min (dist_min, btw_rock) # 최소값 업데이트
                prev = rock
            if remove_cnt > n:
                break

        # 정해진 개수보다 돌 더 부시면, mid 줄이기 (목표 최솟값이 너무 큼을 의미하기 때문)
        if remove_cnt > n: 
            end = mid - 1
        # 그렇지 않으면, mid 늘려보기 (목표 최솟값이 적절하며 목표를 늘려가며 최대값을 찾아야하기 때문)
        else:
            start = mid + 1
            answer = dist_min
            
    return answer

# testcase
distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n)) #4