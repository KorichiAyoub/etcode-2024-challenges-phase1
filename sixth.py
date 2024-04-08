def acmTeam(topics):
    max_known = 0
    max_teams = 0
    
    for i in range(len(topics)):
        for j in range(i+1, len(topics)):
            topics_known = sum(1 for x, y in zip(topics[i], topics[j]) if x == '1' or y == '1')
            if topics_known > max_known:
                max_known = topics_known
                max_teams = 1
            elif topics_known == max_known:
                max_teams += 1
    
    return [max_known, max_teams]

topics = ["11101", "111011", "000110"]
print(acmTeam(topics))
