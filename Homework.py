try:
    age_input = input("Enter your age: ")
    age = int(age_input)
    
    if age < 0:
        raise ValueError
        
    if age % 2 == 0:
        print("The age entered is an even number.")
    else:
        print("The age entered is an odd number.")

except ValueError:
    print("Value Error: Please enter a valid positive whole number for age.")
