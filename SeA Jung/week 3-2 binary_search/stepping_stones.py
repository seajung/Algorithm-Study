'''
def solution(distance, rocks, n):
    rocks.sort()
    distance_btw = [0]* len(rocks)
    
    for i in range(len(rocks)):
    
        if i == len(rocks)-1:
            distance_btw[i] = distance - rocks[i]
        else:
            distance_btw[i] = rocks[i+1] - rocks[i]
    
    distance_btw = [rocks[0]] + distance_btw

    answer = 0
    count = 0
    #print(distance_btw)
    while count < n:
        min_loc = distance_btw.index(min(distance_btw))
        
        if min_loc == 0:
            combined = distance_btw[min_loc]+distance_btw[min_loc+1]
            distance_btw = [combined] + distance_btw[min_loc+2:]

        elif min_loc == len(distance_btw)-1 or distance_btw[min_loc-1] < distance_btw[min_loc+1]:
            combined = distance_btw[min_loc] + distance_btw[min_loc-1]
            distance_btw = distance_btw[:min_loc-1] +[combined] + distance_btw[min_loc+1:]
        else:
            combined = distance_btw[min_loc]+distance_btw[min_loc+1]
            distance_btw = distance_btw[:min_loc] +[combined] + distance_btw[min_loc+2:]
        #print(distance_btw)
        count+=1
        
    #print(distance_btw)
    return min(distance_btw)
    
'''


def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    left = 0
    right = distance
    
    
    while left <= right:
        pivot = (left + right) // 2    
        min_distance = distance
        current = 0  
        count = 0
        for rock in rocks:
            distance = rock - current
            
            # remove rock
            if distance < pivot:  
                count += 1
            else:  
                current = rock  
                min_distance = min(min_distance, distance)
        
        # removed too much
        if count > n:  
            right = pivot - 1
        
        # removed less or suiatble
        else:  
            answer = min_distance
            left = pivot + 1

    return answer