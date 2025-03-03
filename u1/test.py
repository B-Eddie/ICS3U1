nums = input("Please enter the two numbers: ")

numOne = nums[:nums.find(" ")]
numTwo = nums[nums.find(" ")+1:]

product = int(numOne) * int(numTwo)
ones = int(numOne[-1]) + int(numTwo[-1])

print("The product is %i." % product)
print("The product has %i digits." % len(str(product)))
print("The sum of the ones is %i." % ones)
print("The first new number is %s." % (str(numOne[-1]) * len(numOne)))
print("The second new number is %s." % (str(numTwo[-1]) * len(numTwo)))
print("The third new number is %s." % (str(numOne[-1]) * len(numOne) + str(numTwo[-1]) * len(numTwo)))