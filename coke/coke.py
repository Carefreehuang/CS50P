print("Amount Due:50")
money=0
while money<50:
    money_add=int(input("Insert Coin:"))
    if money_add==25 or money_add==10 or money_add==5:
        money+=money_add
    print("Amount Due:",50-money)
print("Change Owed:",money-50)