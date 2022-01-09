def bfs(computers, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        for index, connected in enumerate(computers[v]):
            if connected and (not visited[index]):
                visited[index] = True
                queue.append(index)
    return visited
    
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    while (False in visited):
        start = visited.index(False)
        visited = bfs(computers, start, visited)
        answer +=1
    return answer