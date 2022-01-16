def solution(numbers):
    answer = ''
    str_nums=[]

    for num in numbers:
        str_nums.append(str(num))
            
    str_nums.sort(key=lambda x: x * 3, reverse=True)
        
    for num in str_nums:
        answer += num
            
    # 예외 처리
    if int(answer) == 0:
        answer = "0"
    return answer