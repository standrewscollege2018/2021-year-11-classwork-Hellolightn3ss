
auction = input("what item is up for sale today?")

Reserve_price = input("what is the reserve price")

print("The auction for the", auction,"has begun with the reserve price of $",Reserve_price,)

name = input("whats your name?")
bid = int(input("what's your bid? input as interger"))
condition = 1
true = 1
admin =("admin")

while condition is true:

    print("Highest bid so far is",name,"with $", bid)

    name2 = input("whats your name?")

    bid2 = int(input("what's your bid? input as interger"))

    if bid2 > bid:

        bid = bid2
        name = name2

    if bid2 == -1 and name2 == admin:
        print("congradulations to", name,"for winning", auction,"for $",bid)
        condition = 2




