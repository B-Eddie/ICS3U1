nameOne = input("Enter the name of the first product: ")
nameTwo = input("Enter the name of the second product: ")
nameThree = input("Enter the name of the third product: ")
productOne = float(input("Enter the price of the first product: "))
productTwo = float(input("Enter the price of the second product: "))
productThree = float(input("Enter the price of the third product: "))

total = productOne + productTwo + productThree
tax = total * 0.13

finalTotal = total + tax

print("WOSS Gift Shop Receipt")
print("----------------------")
print("%-10s %10.2f" % (nameOne, productOne))
print("%-10s %10.2f" % (nameTwo, productTwo))
print("%-10s %10.2f" % (nameThree, productThree))
print("----------------------")
print("%-10s %10.2f" % ("HST (13%)", tax))
print("----------------------")
print("%-10s %10.2f" % ("Total:", finalTotal))
