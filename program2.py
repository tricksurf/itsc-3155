numberOne = int(input("Please give the first number: "))
numberTwo = int(input("Please give the second number: "))

numberRange = range(numberOne, numberTwo)
for n in numberRange:
    if n % 7 == 0:
        if n % 5 != 0:
            print(n, end=" ")

