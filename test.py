from functions import calculateTax, readFile, writeFile, currentWorkingDirectory
import math


#@TODO: Refactor code to also accept user name.

userInput = int(input('Please amount: '))
bill = calculateTax(userInput)
print("Total amount to be paid is: " , bill)
print("This is the floored bill " , math.floor(bill))
readFile()
writeFile(bill)
currentWorkingDirectory()
