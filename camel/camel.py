str=input("camelCase:")
new_str=""
for i in range(len(str)):
    if str[i].isupper():
        new_str+="_"+str[i].lower()
    else:
        new_str+=str[i]
print(new_str)