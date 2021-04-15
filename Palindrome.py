def isPalindrome(string):
    left = 0 
    right = len(string) -1 
    while(left < right):
        if(string[left] is not string[right]): return False 
        left+=1
        right-=1
    return True
print(isPalindrome('abba'))