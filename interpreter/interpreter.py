str=input("Expression:")
strlist=str.split()
strlist[0]=int(strlist[0])
strlist[2]=float(strlist[2])
if strlist[1]=="+":
    print(strlist[0]+strlist[2])
elif strlist[1]=="-":
    print(strlist[0]-strlist[2])
elif strlist[1]=="*":
    print(strlist[0]*strlist[2])
elif strlist[1]=="/" and strlist[2]!=0:
    print(strlist[0]/strlist[2])