def solution(clothes):
    answer = 0
    
    # sort by type
    clothes_dic={}
    for [clothes_name, clothes_type] in clothes:
        if clothes_type in clothes_dic.keys():
            clothes_dic[clothes_type].append(clothes_name)
        else:
            clothes_dic[clothes_type]=[clothes_name]
    
    # count combinations
    combinations = 1
    for clothes_type in clothes_dic.keys():
        combinations = combinations * (len(clothes_dic[clothes_type])+1)
    
    answer = combinations -1
    return answer