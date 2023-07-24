def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if not all(ch.isalnum() for ch in s):  #逐一判断是不是字符为字母和数字
        return False
    if not s[0:2].isalpha():
        return False
    flag=False
    for ch in s:             #判断是否字母数字交替
        if ch.isdigit():
            flag=True
        if ch.isalpha() and flag:
            return False
    flag2=True
    for ch in s:
        if ch.isdigit() :
            if ch=='0' and flag2:
                return False
            else :
                flag2=False
    return True

main()