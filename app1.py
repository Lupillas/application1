import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(_word):
    _word=_word.lower()
    if _word in data:
        return data[_word]
    elif len(get_close_matches(_word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(_word,data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(_word,data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't exist. Please double ckeck it"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it"

word= input("Enter word: ")

print(translate(word))
