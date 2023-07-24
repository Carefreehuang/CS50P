def convert(word):
    word=word.replace(":)","🙂")
    word=word.replace(":(","🙁")
    return word
word=input()
word=convert(word)
print(word)