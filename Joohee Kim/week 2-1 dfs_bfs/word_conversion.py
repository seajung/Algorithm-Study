paths = []

def is_similar(word1, word2): # O(1)
    same_count = 0
    word_len = len(word1)
    for i in range(word_len):
        if word1[i] == word2[i]:
            same_count += 1
    if same_count >= word_len - 1:
        return True
    return False


def bfs(graph_dict, root, target):
    visited = []  # node
    queue = [(root, 0)]  # (node, depth)

    while (queue):
        current_node = queue.pop(0)
        
        if current_node[0] == target:
            return current_node[1]
        
        if current_node[0] not in visited:
            visited.append(current_node[0])
            child_lst = graph_dict[current_node[0]]
            depth_lst = [current_node[1] + 1 for i in range(len(child_lst))]
            queue.extend( zip(child_lst, depth_lst) )
        
    return 0


def dfs(graph_dict, root, target, visited): # O(n^2)
    visited.append(root)
    
    if root == target:
        paths.append(visited)
        return
    
    for n in graph_dict[root]:
        if n not in visited:
            dfs(graph_dict, n, target, visited[:])



# with bfs                     
def solution1(begin, target, words):
    answer = 0
    graph_dict = {}
    
    if target not in words:
        return 0
    
    all_words = words + [begin]
    for w in all_words:
        graph_dict[w] = []
    
    for w1 in all_words: # O(n^2)
        for w2 in all_words:
            if (w1 != w2) and is_similar(w1, w2):
                graph_dict[w1].append(w2)    
    
    answer = bfs(graph_dict, begin, target)
    
    return answer


# with dfs
def solution2(begin, target, words):
    answer = 0
    graph_dict = {}
    
    if target not in words:
        return 0
    
    all_words = words + [begin]
    for w in all_words:
        graph_dict[w] = []
    
    for w1 in all_words: # O(n^2)
        for w2 in all_words:
            if (w1 != w2) and is_similar(w1, w2):
                graph_dict[w1].append(w2)    
    
    dfs(graph_dict, begin, target, [])

    paths_len = [len(p)-1 for p in paths]
    answer = min(paths_len)
    
    return answer




# testcase
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution1(begin, target, words))
print(solution2(begin, target, words))