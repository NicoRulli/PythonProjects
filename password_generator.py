#Random Password Generator 
import random
numz = '1234567890'
symz = '"\':;?/>.<,~`!@#$%^&*()_-+={[}]|'
lowercase_letterz = "abcdefghijklmnopqrstuvwxyz"
uppercase_letterz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


lower_list = list(lowercase_letterz) # Creates list of lowercase letters
upper_list = list(uppercase_letterz) # Creates list of uppercase letters
numbers = list(numz) # List of numbers 0-9
symbols = list(symz) # List of symbols/special characters

password = ''
password_strength = ''
while len(password_strength) < 3:
    password_strength = input('Enter your preferred password difficulty (Weak, Strong, Extra Strong): ')


password_strength = password_strength.lower()
password_strength = password_strength.replace(" ", "")

password_length = 0 

if password_strength == 'weak':
    password_length = 8

if password_strength == 'extrastrong':
    password_length = 40

if password_strength == 'strong':
    password_length = 16

print('Your password length will be:', password_length)
upper = random.randint(100,1000) # Creates an upper bound of how many of each character type to use below

letters_used = random.randint(10, upper)
numbers_used = random.randint(10, upper)
symbols_used = random.randint(10, upper)

big_password_len = letters_used + numbers_used + symbols_used

for i in range(big_password_len):
    lower_list_random    = random.randint(0, 25)
    upper_list_random    = random.randint(0, 25)
    numbers_random       = random.randint(0, 9)
    symbol_random        = random.randint(0, 30)

    password = password + lower_list[lower_list_random] + upper_list[upper_list_random] + numbers[numbers_random] + symbols[symbol_random]

last_random = random.randint(0, big_password_len - 20)

password = password[last_random : last_random + password_length - 1] 
print('Your random password is: ', password)
