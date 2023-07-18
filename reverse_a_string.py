#Reverses sentences 

input_sentence = 'Nicolas Rulli is my name '

def reverse(string):
    reversed_string = [] * len(string)
    sentence = string.split()
    for i in range(len(sentence) -1, -1, -1): 
        reversed_string.append(sentence[i])
    return reversed_string

print(reverse(input_sentence))