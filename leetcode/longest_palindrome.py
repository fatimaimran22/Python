def isPalindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return isPalindrome(s,left+1,right-1)

        

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    window={}
    left=0
    max_len=0
    
    for j in len(s):
        if isPalindrome(s,left,j) is True:
            if len(s[left:j+1])> max_len:
                max_len=len(s[left:j+1])
            left+=1
                



        