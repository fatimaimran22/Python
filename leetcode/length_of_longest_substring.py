def lengthofLongestSubstring(s):
    if s==None or len(s)==0:
        return 0
    
    substring=[]
    box=""
    for i in range(len(s)):
        box=s[i]
        for j in range(i+1,len(s)):
            if s[j] not in box:
                box+=s[j]
            else:
                substring.append(box)
                break
        substring.append(box)
    max_len=0
    for subs in substring:
        if len(subs)>max_len:
            max_len=len(subs)

    return max_len


print(lengthofLongestSubstring(" "))
