def solution(clothes):
    number_dict = dict()
    for [a, b] in clothes:
        if not b in number_dict:
            number_dict[b] = 1
        else:
            number = number_dict.get(b)
            number_dict[b] = number + 1
    number_list =  number_dict.values()
    #print(number_list)
    answer = 1
    for i in number_list:
        answer = answer * (i+1)
    answer = answer -1
    return answer
