def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    left = 0
    right = distance
    
    while (left <= right):
        mid = int((left + right) / 2)
        
        count = 0
        move_rock = 0
        
        for i in range(len(rocks)):
            if (rocks[i] - move_rock < mid): # 각 바위 사이의 거리가 현재(mid)보다 작은 경우
                count += 1
            else:
                move_rock = rocks[i]
                
        if count > n: # 현재(mid)보다 거리가 작은 경우가 좀 많음
            right = mid - 1
        else:
            left = mid + 1 
            answer = mid
            
    return answer
