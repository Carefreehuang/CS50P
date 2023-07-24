grocery={}
while True:
    try:
        item=input("").upper()
    except EOFError:
        print()
        break
    if item in grocery:
        grocery[item] += 1
    else:
        grocery[item] = 1
for item,cnt in sorted(grocery.items()):
    print(f"{cnt} {item}")
