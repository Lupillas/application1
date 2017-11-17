import json

data = json.load(open("data.json"))

def translate(_word):
    _word=_word.lower()
    if _word in data:
        return data[_word]
    else:
        return "The word doesn't exist. Please double check it"

word= input("Enter word: ")

print(translate(word))
