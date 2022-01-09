def solution(prices):
    
    L = len(prices)
    answer = [0]*L
    
    for i in range(L):
        for j in range(i+1, L):
            
            answer[i] += 1
            
            if(prices[i]>prices[j]):
                break
            
    return answer
        
