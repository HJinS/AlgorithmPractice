def solution(table, languages, preference):
    
    pref_map = {}
    score_map = {}
    
    for idx, lan in enumerate(languages):
        pref_map[lan] = preference[idx]    
    
    for row in table:
        pref = list(row.split(' '))
        score_map[pref[0]] = 0
        sc = 5
        score = 0
        for i in range(1, len(pref)):
            if pref[i] in pref_map:
                score += sc * pref_map[pref[i]]
            sc -= 1
        score_map[pref[0]] = score
            
    listed_item = list(score_map.items())
    
    listed_item.sort(key = lambda x : (-x[1], x[0]))
    return listed_item[0][0]