def getscore(jewels):
    score = 0
    i=0
    while i< (len(jewels)-1):
        if(jewels[i]==jewels[i+1]):
            score += 1
            jewels = jewels[0:i]+jewels[i+2:]
            i = max(0,i-1)
        else: 
            i+=1
    return score

print(getscore("aabbaaa"))