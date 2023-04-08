import random
import string

while True:
    length = input("Enter the password length: ")
    while not length.isdigit() or int(length) <= 0:
        print("Invalid input. Please enter number, that`s more than 0")
        length = input("Enter the password length: ")
    length = int(length)

    uppercase = input("Add capital letters (yes/no)? ").lower()
    while uppercase != 'yes' and uppercase != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        uppercase = input("Add capital letters (yes/no)? ").lower()
    uppercase = uppercase == 'yes'

    lowercase = input("Add lowercase letters (yes/no)? ").lower()
    while lowercase != 'yes' and lowercase != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        lowercase = input("Add lowercase letters (yes/no)? ").lower()
    lowercase = lowercase == 'yes'

    numbers = input("Add numbers (yes/no)? ").lower()
    while numbers != 'yes' and numbers != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        numbers = input("Add numbers (yes/no)? ").lower()
    numbers = numbers == 'yes'

    special = input("Add signs (yes/no)? ").lower()
    while special != 'yes' and special != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        special = input("Add signs (yes/no)? ").lower()
    special = special == 'yes'

    characters = "!@#$%^&*_-*/№;:()+"
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation

    if not characters:
        print("Error: Unable to create password while all categories = 'No'.")
        continue
    password = ''
    for i in range(length):
        password += random.choice(characters)

    print("Your password: ", password)
    break