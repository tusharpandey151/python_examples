days = 365
isOnline = False
name = input("What is your name? ")
birthYear = input("What is your birth year? ")
age = 2024 - int(birthYear)
print(name + "'s Age is" , age, "and his online status is ", isOnline)
#Strings are immutable.. all below string methods return new String.
print(name.replace("s","g"))
print(name.upper())
print(name.find("us"))
print("ar" in name)
firstNum = input()
secondNum = input()
print(type(firstNum) , float(firstNum) + float(secondNum))