
vowels = {
    'a': True,
    'e': True,
    'o': True,
    'u': True,
    'i' : True
}

def countVowels(string):
    count = 0 
    for char in string:
        if(vowels.get(char)): count+=1
    return count

print(countVowels('hello'))