def solution(citations):
    citations.sort(reverse=True)
    for i , number in enumerate(citations):
        if i >= number:
            return i
    return len(citations)
