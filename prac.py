agent1 = input("Please enter the first agent: ")
price1 = int(input("Please enter the sale price for %s: " % agent1))
agent2 = input("Please enter the second agent: ")
price2 = int(input("Please enter the sale price for %s: " % agent2))
agent3 = input("Please enter the third agent: ")
price3 = int(input("Please enter the sale price for %s: " % agent3))
commission1 = price1 * 0.025
commission2 = price2 * 0.025
commission3 = price3 * 0.025
print("%-20s %8s %10s" % ("Agent", "Price", "Commission"))
print("%-20s %8i %10.2f" % (agent1, price1, commission1))
print("%-20s %8i %10.2f" % (agent2, price2, commission2))
print("%-20s %8i %10.2f" % (agent3, price3, commission3))