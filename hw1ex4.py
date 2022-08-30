#Getting information from the user
apples = int(input("Please enter the number of apples:"))
bananas = int(input("Please enter the number of bunches of bananas:"))
oranges = int(input("Please enter the number of oranges:"))
lemons = int(input("Please enter the number of lemons:"))

#Calculating the price of Apples
applescos = 0.5*apples
applescost = round(applescos, 2)

#Calculating the price of Bananas
bananascos = 2.50*bananas
bananascost = round(bananascos, 2)

#Calculating the price of Oranges
orangescos = 0.75*oranges
orangescost = round(orangescos, 2)

#Calculating the price of Lemons
lemonscos = 1.25*lemons
lemonscost = round(lemonscos, 2)

#Running feedback part one
print("\n")
print(f"The total bill for {apples} apples is: ${applescost:.2f}")
print(f"The total bill for {bananas} bunches of bananas is: ${bananascost:.2f}")
print(f"The total bill for {oranges} oranges is: ${orangescost:.2f}")
print(f"The total bill for {lemons} lemons is: ${lemonscost:.2f}")


#Adding totals
totalitems = apples + bananas + oranges + lemons

totalcost = applescost + bananascost + orangescost + lemonscost

#Running feedback part two
print("\n")
print("The total number of items purchased is:", totalitems)
print(f"The overal total bill is: ${totalcost:.2f}")