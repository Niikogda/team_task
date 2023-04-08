
import random
import string

length = int(input("Введіть довжину паролю: "))
uppercase = input("Включити великі літери (так/ні)? ").lower() == 'так'
lowercase = input("Включити маленькі літери (так/ні)? ").lower() == 'так'
numbers = input("Включити цифри (так/ні)? ").lower() == 'так'
special = input("Включити знаки (так/ні)? ").lower() == 'так'

# Створення списку доступних символів
characters = ''
if uppercase:
    characters += string.ascii_uppercase
if lowercase:
    characters += string.ascii_lowercase
if numbers:
    characters += string.digits
if special:
    characters += string.punctuation
    