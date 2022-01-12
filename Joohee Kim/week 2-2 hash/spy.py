def solution(clothes):
    clothes_dict = {}   # dict{type: # of clothes}
    
    for cloth in clothes:
        type = cloth[1]
        if type not in clothes_dict.keys():
            clothes_dict[type] = 1
        else:
            clothes_dict[type] += 1
    
    answer = 1
    for _, value in clothes_dict.items():
        answer *= value + 1
    answer -= 1    
    
    return answer

# testcase
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
# 5