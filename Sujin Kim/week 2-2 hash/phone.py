def solution(phone_book):
    
    L = len(phone_book)
    
    if(L == 1):
        return True
    
    phone_book.sort()
    
    for i in range(L-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            sub_len = len(phone_book[i])
            if phone_book[i + 1][:(sub_len)] == phone_book[i]:
                return False
    return True
                
