
def solution1(phone_book):
    answer = True
    phone_dict = {}
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return answer
    
# with HASH
def solution2(phone_book):
    answer = True
    phone_dict = {}
    for num in phone_book:
        phone_dict[num] = 0
    for num in phone_book:
        for i in range(len(num)-1):
            if num[:i+1] in phone_dict.keys():
                return False

    return answer

phone_book = ["119", "97674223", "1195524421"]	

print(solution1(phone_book))
print(solution2(phone_book))