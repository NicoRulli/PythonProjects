#Code must guess a number the user chooses between 1 and 100. 
#User will input 'higher' or 'lower' to let the code know where 
#its guess is compared to the right answer. 

import random 

beg = 0                 #lower bound
max = 100               #upper bound
array1 = []

for i in range(0,100,1):
    array1.append(i)

print("Welcome to the number guessing game!")
def search(array, low, upper, rand_lower, rand_higher):

    guess = random.randint(rand_lower, rand_higher)
    print("My guess is", guess)
    hl = input("Is your number higher or lower?")
    hl = hl.lower()

    if hl == 'exit':
        print("Number guessed!")
    
    elif hl == 'higher':
        search(array, guess + 1, upper, guess + 1, upper)
    
    elif hl == 'lower':
        search(array, low, guess - 1, low, guess - 1)

search(array1, beg, max, 0, 100) 



