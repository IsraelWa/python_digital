print("Welcome to the market.\n\nPrices:\n---------------\nTomato: 3 NIS\nCucamber: 2 NIS\nCola: 5 NIS\nChicken: 20 NIS\n\n")

tom=int(input("Type how many tomatos:"))
cuc=int(input("Type how many cucambers:"))
col=int(input("Type how many colas:"))
chk=int(input("Type how many chickens:"))

print("\n\nSummary of your order:\n-------------------------")
print("Tomatos: " + str(tom) + "\nCucambers: " + str(cuc) + "\nColas: " + str(col) + "\nChickens: " + str(chk))

Smry=tom*3 + cuc*2 + col*5 + chk*20

print("Total: " + str(Smry) + " NIS before tax.\n")
print("Total for pay: " + str("%.2f" % (Smry*1.17)) + " NIS including tax.")