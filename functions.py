def greet(first_name, last_name): # Parameters
    print(f"Hi {first_name} {last_name}")


greet("Tushar" , "Pandey") #Arguments


def get_greet(first_name, last_name="Pandey"): # Parameters -- last name has optional parameter  -- IMP - Optional Parameters can only come after all required paramters
    return (f"Hi {first_name} {last_name}")


print(get_greet(first_name="Tushar" , last_name="Pandey"))#keyword argument before the argument

print("Default last name " + get_greet(first_name="Tushar"))#keyword argument before the argument


print(greet("Tushar" , "Pandey"))# here we get none -- as this function does not return anything.. all functions return null by default unless we return something explicitly

def multiply(*numbers):# Takes multiple entries - these entries are passed as tuple
    i = 1
    for number in numbers:
        i*=number
    return i

print(multiply(3,5,6,7,8))


def save_user(**userData): # using double * again takes multiple entries but with keyword argument making the input type a dictionary
    print("ID: ", userData["id"])
    print("Name: ", userData['name'])
    print("Age : ", userData["age"])


save_user(id=345, name="Tushar Pandey", age = 31)

message = "test"

def funct():
    global message# This is a way to update the global variable in the scope of a method -- IMP Bad Practice Avoid Global Variable .. And definetly avoid changing the global in other scope
    message = "tushar"

print(message)
funct()
print(message)

def testFunct():
    message = "Pandey"

testFunct()

print(message)# This still prints tushar as updated above in funct -- why ? because in testFunct - python expects this message variable to be a new variable shadowing the global message

def fizz_buzz(input):
    number = int(input)
    if(number%15==0):
        print("fizzbuzz")
    elif(number%3==0):
        print("fizz")
    elif(number%5==0):
        print("buzz")
    else:
        print(number)

fizz_buzz(25)
fizz_buzz(7)
fizz_buzz(30)
fizz_buzz(21)
