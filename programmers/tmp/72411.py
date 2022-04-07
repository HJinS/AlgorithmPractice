import itertools
def solution(orders, course):
    ordered = []
    for order in orders:
        mask = 0
        for c in order:
            num_mask = 1 << (ord(c) - ord('A'))
            mask |= num_mask
        ordered.append(mask)

        
    ans = set()
    candi = {}
    ans_dic = {}
    for order in orders:
        for course_cnt in course:
            order_list = list(order)
            if course_cnt > len(order_list):
                break
            
            for item in itertools.combinations(order_list, course_cnt):
                total_mask = 0
                for menu in item:
                    mask = 1 << (ord(menu) - ord('A'))
                    total_mask |= mask
                cnt = 0
                for order_set_item in ordered:
                    if order_set_item & total_mask == total_mask:
                        cnt += 1
                if cnt >= 2:
                    
                    list_item = list(item)
                    list_item = sorted(list_item)
                    item_length = len(list_item)
                    if item_length in candi:
                        if candi[item_length] < cnt:
                            candi[item_length] = cnt
                            ans_dic[item_length] = {"".join(list_item)}
                        elif candi[item_length] == cnt:
                            ans_dic[item_length].add("".join(list_item))
                    else:
                        candi[item_length] = cnt
                        ans_dic[item_length] = {"".join(list_item)}

    ans = []
    
    for item in ans_dic.values():
        for menu in item:
            ans.append(menu)
            
    ans.sort()
    return ans