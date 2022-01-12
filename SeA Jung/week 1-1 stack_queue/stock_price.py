def solution(prices):
    
    stack = []
    answer = [0 for i in range(len(prices))]
    
    for curr_time, price in enumerate(prices): 
        while stack and price < prices[stack[-1]]:
            price_time = stack.pop()
            answer[price_time] = curr_time - price_time
        stack.append(curr_time)
    
    while stack:
        price_time = stack.pop()
        answer[price_time] = len(prices) - 1 - price_time

    return answer 