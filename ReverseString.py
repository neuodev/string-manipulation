def reverseString(string):
    stack = []
    strArray = []
    newString = ''
    for char in string:
        stack.append(char)
    for i in range(len(stack)):
        strArray.append(stack.pop(len(stack) -1 ))
    for char in strArray:
        newString+=char
    print(newString)
reverseString('hello')