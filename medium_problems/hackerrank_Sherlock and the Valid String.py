def isValid(s):
    dic = dict() # Count ocurrences of char in s
    dic2 = dict() # key = occurences of char, value = num of char
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    for x in dic.items():
        occurences = x[1]
        dic2[occurences] = dic2.get(occurences, 0) + 1
    if len(dic2) == 1:
        return "YES"
    elif len(dic2) == 2:
        # now we have two pairs
        # (occurences : num of char)
        #  occurences of bigger num of char should be one less than occurences of small num of char ( it should be 1)
        lst = [x for x in dic2.items()]
        p1 = lst[0]
        p2 = lst[1]
        if p1[1] > p2[1]:
            freq = p1
            rare = p2
        else: # or two occurences have same numbo
            freq = p2
            rare = p1
        if rare[1] == 1:
            if rare[0] == 1 or (rare[0] - 1) == freq[0]:
                return "YES"
        return "NO"
    else:
        return "NO"