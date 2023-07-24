def main():
    str=input("What time is it?")
    if str.endswith("a.m."):
        strlist=str.split()
        str=strlist[0]
        time=convert(str)
    elif str.endswith("p.m."):
        strlist=str.split()
        str=strlist[0]
        time=convert(str)+12
    else:
        time=convert(str)

    if time>=7 and time<=8:
        print("breakfast time")
    elif time>=12 and time<=13:
        print("lunch time")
    elif time>=18 and time<=19:
        print("dinner time")
def convert(time):
    timelist=time.split(":")
    hours=int(timelist[0])
    minutes=float(timelist[1])
    time=hours+minutes/60
    return time

if __name__ == "__main__":
    main()