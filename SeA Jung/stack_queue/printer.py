def solution(priorities, location):
    print_pending_list = [i for i in range(len(priorities))]
    priorities_check = priorities[:]
    printed = []
    answer = 0
    while not (location in printed):
        curr_doc = print_pending_list[0]
        curr_priority = priorities[print_pending_list[0]]
        if curr_priority >= max(priorities_check):
            # print
            printed.append(curr_doc)
            priorities_check[curr_doc] = -1
        else:
            print_pending_list.append(curr_doc)
            
        del print_pending_list[0]
    answer = len(printed)
    return answer