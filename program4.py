numberOfItems = int(input("Number of items: "))

listOfNames = []
listOfPrices = []

for n in range(0, numberOfItems):
    itemName, itemPrice = input("Enter item: ").split()
    listOfNames.append(itemName)
    listOfPrices.append(int(itemPrice))

zippedList = list(zip(listOfNames, listOfPrices))

zippedList = sorted(zippedList, key = lambda x: x[1])

for a, b in zippedList:
    print(a, b)
