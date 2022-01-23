def solution(N, number):
    answer = 0
    if N == number:
        return 1
    # num_lst: 첫번째 index가 사용된 숫자(N) 개수를 의미함
    num_lst = [[]] + [[int(str(N)*(i+1))] for i in range(8)]    # N 최대 8개 사용가능
    
    for i in range(2,9):    # i = 연산해서 나온 결과값을 만드는데 사용된 N의 개수
        for k in range(i-1,0,-1):   # 역순 --> num2가 가장 작은 숫자 개수부터 돌도록
            for num1 in num_lst[k]:  # i=8   k=7,6..,1   i-k=1,2,..7
                for num2 in num_lst[i-k]:
                    a = num1 + num2
                    if a != 0:
                        num_lst[i].append(a)
                    
                    a = num1 - num2
                    if a != 0:
                        num_lst[i].append(a)
                    
                    num_lst[i].append(num1 * num2)
                    
                    a = num1 // num2
                    if a != 0:
                        num_lst[i].append(a)
                
        if number in num_lst[i]:
            answer = i
            break
        
        num_lst[i] = list(set(num_lst[i]))
    
    if answer == 0:
        return -1
        
    return answer

# testcase
N = 5
number = 31168
print(solution(N, number)) #-1