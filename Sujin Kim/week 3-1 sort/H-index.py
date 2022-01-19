def solution(citations):
    maxx = 0
    for i in range(max(citations)):
        count = 0
        for j in citations:
            if(j>=i):
                count += 1
        if(count >= i):
            if(maxx < i):
                maxx = i
    return maxx
