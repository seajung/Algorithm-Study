def Find_network(n, computers, visited, visit_node):
    visited[visit_node] = True
    for node in range(n):
        if (node != visit_node):
            if (computers[visit_node][node] == 1):
                if(visited[node] == 0):
                    Find_network(n, computers, visited, node)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for node in range(n):
        if (visited[node]==0): # list는 global?, mutable-> 재할당이 아닌 수정
            Find_network(n, computers, visited, node)
            answer += 1
    return answer

