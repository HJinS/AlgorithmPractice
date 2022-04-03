def solution(id_list, report, k):
    ban_dict = {}
    report_dict = {}
    ban_list = [0 for i in range(len(id_list))]
    ans = [0 for i in range(len(id_list))]
    user_info = {}
    for idx, user in enumerate(id_list):
        report_dict[user] = []
        user_info[user] = idx
    
    for r in report:
        user_to, user_from = r.split(' ')
        if user_from in report_dict[user_to]:
            continue
        report_dict[user_to].append(user_from)
        ban_list[user_info[user_from]] += 1
    
    for idx, user in enumerate(id_list):
        cnt = 0
        list_item = report_dict[user]
        for banned in list_item:
            if ban_list[user_info[banned]] >= k:
                ans[idx] += 1
                
    return ans