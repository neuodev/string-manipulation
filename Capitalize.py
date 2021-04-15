def capitalize(string):
    text = 'trees are      beautiful'
    textArr =  text.split(' ')
    for i in range(len(textArr)):
      textArr[i] = textArr[i].capitalize()
    newString = ' '.join(textArr)
    print(newString )
capitalize('trees are beautiful')
    