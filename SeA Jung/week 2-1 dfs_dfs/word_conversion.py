def can_change(word1, word2):
    count = 0 
    for i in range(len(word1)):
        if not word1[i] == word2[i]:
            count+=1
    if count == 1:
        return True
    return False
    
def solution(begin, target, words):
    
    graph = dict(zip(words, [[] for i in range(len(words))]))
    
    answer = 0
    if not target in words:
        return answer
    
    # make graph
    for i, word1 in enumerate(words):
        for j,word2 in enumerate(words[i+1:]):
            if can_change(word1, word2):
                graph[word1].append(word2)
                graph[word2].append(word1)
    # add root
    graph[begin]=[]
    for word in words:
        if can_change(begin, word):
            graph[begin].append(word)
                
    #find shortest path
    distance = dict(zip(words, [0 for i in range(len(words))]))
    distance[begin]=0
    visited = dict(zip(words, [False for i in range(len(words))]))
    visited[begin]= True
    
    queue = [begin]

    while queue:
        curr_word = queue.pop(0)
        for next_word in graph[curr_word]:
            if not visited[next_word]:
                queue.append(next_word)
                visited[next_word] = True
                distance[next_word] = distance[curr_word] + 1
                if next_word == target:
                    return distance[next_word]

    return answer