def solution(genres, plays):
    answer = []
    genres_count_dict = dict()
    L = len(genres)
    for i in range(L):
        if not genres[i] in genres_count_dict:
            genres_count_dict[genres[i]] = plays[i]
        else:
            number = genres_count_dict.get(genres[i])
            genres_count_dict[genres[i]] = number + plays[i]
    sorted_dict = sorted(genres_count_dict.items(), key = lambda item: item[1], reverse = True)
   
    for (gen, cou) in sorted_dict:
        sub_list = dict()
        for i in range(L):
            if(genres[i] == gen):
                sub_list[i] = plays[i]
        sort_sub = sorted(sub_list.items(), key = lambda item: item[1], reverse = True)
        answer.append(sort_sub[0][0])
        if(len(sort_sub) > 1):
            answer.append(sort_sub[1][0])
    
    return answer
