temp = 30

if(temp>30):# Indentation means block of code
    print("Hot Day")
elif temp < 30: 
    print("Cool Day")
else: 
    print ("Okayis day")


while temp<100:
    print(temp//5* "T") # Multiplying with a string will print that string that many times
    temp+=5

newList = ["Tushar", "Antara", "Sunil", "Pratibha", "Ravi", "Neelima"]
print(newList[0])
print(newList[0:3])
newList[0] = "Tushar Pandey"
newList.insert(0,"Pandey")
print(newList[0:5])
newList.remove("Pandey")
print(newList)
print("Tushar Pandey" in newList)
print(len(newList))
newList.clear()
print(newList)
for name in newList:  # For loop to iterate over list
    print("Name is: " , name)

# Range Objs 

for number in range(6): # upto and not including the number passed
    print(number)

for number in range(5,11): # from 5 to 11 (11 not included)
    print(number)

for number in range(1,20,2): # from 1 to 20 (not included) with increments of 2 - 1, 3,5,7 ... upto 19
    print(number)


#Tuples

tupleExample = (1,2,3) # cannot add or remove anything from this... they are immutable .. iterate as we do