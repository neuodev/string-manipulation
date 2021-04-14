def removeDuplicate(string):
    newString = ''
    for i in range(len(string) -1 ):
        print (string[i] , string[i+1])
        if string[i] == string[i+1]: continue
        else: newString+=string[i]
    return newString
removeDuplicate('Hellooo!!')