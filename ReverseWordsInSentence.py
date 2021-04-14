def reverse(sentence):
     newString = sentence.split(' ')
     newString.reverse()
     string = ' '
     return string.join(newString)
print(reverse('Trees are beautiful'))