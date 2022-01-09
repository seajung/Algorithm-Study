def make_words(begin, target, words, visited):
    level = 0
    stack = [begin]
    
    while stack:
        next_nodes = [] # 다음 level의 node 전부 저장
        while stack: # 한 level에 대해 전부 돌리기
            now = stack.pop()
            
            if (now == target):
                return level
        
            for i in range(len(words)):
                
                if (visited[i] == 0): # 방문 안한 것만
            
                    difference = 0
            
                    for now_al,word_al in zip(now, words[i]): 
                    # !! 알파벳끼리 비교할 수 있게 해줌. 기억해둘함수 !!
                        if now_al!=word_al:
                            difference += 1
                    
                    if difference == 1:
                        visited[i] = 1
                        next_nodes.append(words[i])
                    
        stack = next_nodes
        level += 1
        
    return 0

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [0]*(len(words))

    answer = make_words(begin, target, words, visited)

    return answer
