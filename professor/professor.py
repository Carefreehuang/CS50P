import random


def main():
    level=get_level()
    score=0
    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        result=x+y
        i=0
        while True:
            try:
                print(str(x) + " + " + str(y) + " = ",end="")
                guess=int(input())
            except ValueError:
                    pass
            if guess==result:
                score+=1
                break
            elif guess!=result and i<2:
                print("EEE")
                i+=1
            else:
                print(str(x) + " + " + str(y) + " = " + str(result))
                break



def get_level():
    while True:
        level=input("Level:").strip()
        if level=="1" or level=="2" or level=="3":
            level=int(level)
            return level

def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
         return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)




if __name__ == "__main__":
    main()