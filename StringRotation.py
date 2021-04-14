def isRotation(first, second):
    firstIdx = 0 
    secondIdx = 0
    while secondIdx < len(second):
        if second[secondIdx] == first[firstIdx]: break
        secondIdx+=1
   

    while firstIdx < len(first):
          if secondIdx == len(second) : secondIdx = 0
          if first[firstIdx] is not second[secondIdx]: return False
          firstIdx+=1
          secondIdx+=1
    return True

print(isRotation('ABCD','ADBC'))