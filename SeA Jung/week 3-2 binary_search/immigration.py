'''
import math

def solution(n, times):

    answer = 0
    depth = 0
    root = 1
    root_depth = 1
    check_list = []
    
    passed_people = 0
    
    # finding root
    while depth < 30:
        passed_people = 0

        for time in times:
            passed_people += root // time
            if passed_people >= n:
                break
            
        if passed_people < n:
            root *= 2
            depth +=1
        else: 
            break
            
    check_list = [False] * root

    if root == 1:
        return root
    
    root = root //2
    print(root)
    root_depth = depth
    node = root
    
    # binary search
    while depth > 0:
        passed_people = 0

        for time in times:
            passed_people += node // time
        
        left_child = node - 2**(depth-2)
        right_child = node + 2**(depth-2)
              
        # search right  
        if passed_people < n :
            node = right_child
        # search left
        else:
            check_list[node] = True
            node = left_child
        depth -=1

    if True in check_list:
        answer = check_list.index(True)
    else:
        answer =  2 * root
        
    return answer
    '''


def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left <= right:
        
        pivot = (left + right) //2
        passed_people =0
        for time in times:
            passed_people += pivot // time
            
            if passed_people >= n:
                break
                
        if passed_people >= n:
            answer = pivot
            right = pivot -1
            
        else:
            left = pivot +1
            
    return answer