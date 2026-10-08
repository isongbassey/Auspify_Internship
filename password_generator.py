import random
import string

try:
    length = int(input("Enter password length: "))
    if length <= 5:
        raise ValueError("Password length must be greater than 5")

    number_of_passwords = int(input("Enter the number of passwords you want to generate: "))
    if number_of_passwords <=0:
        raise ValueError("Number of password must be greater than 0")
    
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    characters = letters + numbers + symbols

    for i in range(number_of_passwords):
        password = ""
        for x in range(length):
            password = password + random.choice(characters)

        print("Generate Password:", password)

except ValueError as error:
    print(f"Error: error")

else:
    print("Password Generation Completed Successfully")

finally:
    print("Thank You for using Password Generator")