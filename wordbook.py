import json
from difflib import get_close_matches

elements = json.load(open("wordbook\wordbook.json"))

def findmeaning(word):
    if word.lower() in elements:
        return(elements[word.lower()])
    elif word.upper() in elements:
        return(elements[word.upper()])
    elif word.title() in elements:
        return(elements[word.title()])
    elif len(get_close_matches(word,elements.keys()))>0 :
        closestmatch = (get_close_matches(word,elements.keys())[0])
        userinput = input("Are you looking for %s instead ?(Y/N): "%closestmatch)
        userinput = userinput.upper()
        if userinput == 'Y':
            return elements[get_close_matches(word,elements.keys())[0]]
        elif userinput == 'N':
            return "I can't find this word,I'm sorry."
        else:
            return "Sorry I can't find the word."
    else:
        return("I can't find the word.Pls check for spelling.")

word = input("Enter any word: ")

output = findmeaning(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
