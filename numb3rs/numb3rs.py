import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$" #判断是否是三位数字构成
    if re.match(pattern,ip):
        i=ip.split(".")
        for item in i:
            if int(item)<0 or int(item) >255:
                return False
            else:
                return True
    else:
        return False



if __name__ == "__main__":
    main()