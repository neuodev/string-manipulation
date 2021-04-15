def isAnagram(first, second):
    first = ''.join(sorted(first))
    second = ''.join(sorted(second))
    if(first == second): return True
    return False

print(isAnagram('abcd' , 'adbe'))