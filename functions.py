def greet(first_name, last_name): # Parameters
    print(f"Hi {first_name} {last_name}")


greet("Tushar" , "Pandey") #Arguments


def get_greet(first_name, last_name="Pandey"): # Parameters -- last name has optional parameter  -- IMP - Optional Parameters can only come after all required paramters
    return (f"Hi {first_name} {last_name}")


print(get_greet(first_name="Tushar" , last_name="Pandey"))#keyword argument before the argument

print("Default last name " + get_greet(first_name="Tushar"))#keyword argument before the argument


print(greet("Tushar" , "Pandey"))# here we get none -- as this function does not return anything.. all functions return null by default unless we return something explicitly

