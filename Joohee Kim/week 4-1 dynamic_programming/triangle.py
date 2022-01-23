def solution(triangle):
    tri_sum = triangle[:]
    
    for i in range(len(triangle)):
        if i == 0:
            continue
        for j in range(i+1):
            if j == 0:  # 첫번째
                tri_sum[i][0] += triangle[i-1][0]
            elif j == i:    # 마지막
                tri_sum[i][-1] += triangle[i-1][-1]
            else:   # 중간
                if triangle[i-1][j-1] > triangle[i-1][j]:
                    tri_sum[i][j] += triangle[i-1][j-1]
                else:
                    tri_sum[i][j] += triangle[i-1][j]
    
    answer = max(tri_sum[-1])
    return answer