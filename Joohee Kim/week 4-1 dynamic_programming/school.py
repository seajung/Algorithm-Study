def solution(m, n, puddles):
    mn_array = [[0 for i in range(m+1)] for j in range(n+1)]    # memoization
    answer = dp(1, 1, n, m, puddles, mn_array) % (10**9+7)
    return answer

def dp(x1, y1, x2, y2, puddles, mn_array): # (x1,y1) --> (x2,y2) 경우의 수 반환
    if x1>x2 or y1>y2:  # 범위 초과
        return 0
    if x1==x2 and y1==y2:   # 목표점 도달
        return 0
    
    if [y1, x1] in puddles: # 물에 잠긴 지역 스킵
        return 0
    
    if (x2-x1)*(y2-y1) == 0 and (x1+1 == x2 or y1+1 == y2): # 목표점 바로 직전 칸
        return 1

    if mn_array[x1][y1] == 0:   # 계산한 적 없는 곳만 계산
        mn_array[x1][y1] += dp(x1, y1+1, x2, y2, puddles, mn_array)
        mn_array[x1][y1] += dp(x1+1, y1, x2, y2, puddles, mn_array)
    
    return mn_array[x1][y1]