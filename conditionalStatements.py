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
print(newList[0:5])