
import random
import string

length = int(input("Enter the password length: "))
uppercase = input("Add capital letters (yes/no)? ").lower() == 'yes'
lowercase = input("Add lowercase letters (yes/no)? ").lower() == 'yes'
numbers = input("Add numbers (yes/no)? ").lower() == 'yes'
special = input("Add signs (yes/no)? ").lower() == 'yes'

characters = ''
if uppercase:
    characters += string.ascii_uppercase
if lowercase:
    characters += string.ascii_lowercase
if numbers:
    characters += string.digits
if special:
    characters += string.punctuation
    

password = ''
for i in range(length):
    password += random.choice(characters)

print("Your password: ", password)