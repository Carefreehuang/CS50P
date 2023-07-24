names=[]
while True:
    try:
        name=input("Name:").strip()
        names.append(name)
    except EOFError:
        print()
        break
print("Adieu, adieu, to ",end="")
if len(names)==1:
    print(names[0])
elif len(names)==2:
    print(names[0] + " and " + names[1])
else:
    for i in range(len(names)):
        if i!=len(names)-1:
           print(names[i]+",",end="")
        else :
           print("and "+names[i])
