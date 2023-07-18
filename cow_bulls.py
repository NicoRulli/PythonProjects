print("Welcome to the Cows and Bulls Game!")
import random
end_game = False
randNum = random.randint(1000,9999)
print('randNum', randNum)

random_str = str(randNum)
random_as_list = list(random_str)

count = 0
num_cows = 0
num_bulls = 0

while end_game == False:
    guess = input("Enter a number: ")
    guess_as_str = list(guess)
    count = count + 1

    for i in range(len(random_str)):
        if random_str[i] == guess[i]:
            num_cows = num_cows + 1
            
        else: 
            num_bulls = num_bulls + 1

    if guess == str(randNum):
        end_game = True
        print('Well done! You guessed the right number! It took you' ,count, 'guesses to win')

    else:
        end_game = False
        print(num_cows, 'cows', num_bulls, 'bull(s)')
    num_bulls = 0
    num_cows  = 0
    