name=input("Enter your full name: ")
mail=input("Enter your mail: ")
age=int(input("Enter your age: "))

print("\n\nDetails you typed:\nName: " + name + "\nMail: " + mail + "\nAge: " + str(age))

print("\n\nRevers Name: " + name[::-1])

print("\n3 times age: " + str(age*3) + "\n\n")

strFind=input("Type the string to find in your full name: ")
print("Is " + strFind + " in the name? ")
print(strFind in name)