def mostRepeated(string):
    freqCounter = {}
    count = 0 
    char = string[0]
    for char in string:
        if freqCounter.get(char): freqCounter[char]+=1
        else: freqCounter[char] = 1

    for key in freqCounter:
        if freqCounter[key] > count: 
            count = freqCounter[key]
            char = key 
   return char 
mostRepeated('Hellooo!!')