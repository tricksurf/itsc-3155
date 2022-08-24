inputString = input("Please enter a string of length 2 or more: ")
if len(inputString) < 2:
    print("String length is less than 2.")
else:
    print(inputString[0] + inputString[1] + inputString[len(inputString) - 2] + inputString[len(inputString) - 1])
