word=input("Greeting:")
word=word.lower().strip()
word5=word[0:5]
word1=word[0:1]
if word5=="hello":
    print("$0")
elif word1=="h":
    print("$20")
else:
    print("$100")