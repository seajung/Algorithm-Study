def solution(priorities, location):
    answer = 0
    queue = priorities.copy() # 복사할 때 주의
    L = len(priorities)
    index = list(range(L))
    
    if(L==1):
        return 1
    
    for i in range(L):
        
        if(i==(L-1)): # 2, 5, 18 런타임
            return L
        
        while (queue[i] < max(queue[(i+1):])):
            a = queue.pop(i)
            queue.append(a)
            
            b = index.pop(i)
            index.append(b)
            
        if(index[i] == location):
            return (i+1)
