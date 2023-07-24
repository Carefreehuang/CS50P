import random
import sys
while True:
    level=input("Level:")
    if level.isdigit() and int(level)>0:
        break
    elif level :
        pass

level=int(level)
n=random.randint(1,level)
while True:
    number=int(input("Guess:"))
    if number<n:
        print("Too small!")
    elif number>n:
        print("Too large!")
    else:
        print("Just right!")
        sys.exit()


