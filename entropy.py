import numpy as np
import math as math

text_file = open("second_example.txt","r");

characters = {}
character_frequency = {}
doublets_frequency = {}
number_of_characters = 0

for line in text_file:
    for character in line:
        number_of_characters += 1
        if str(character) in characters:
            characters[str(character)] += 1
        else:
            characters[str(character)] = 1 
            
text_file.close()

for character, number_of_repetitions in characters.items():
    character_frequency[character] = number_of_repetitions / number_of_characters

q = len(characters)
print("Number of different elements: ", q)

# calculate the maximal entropy of the source without any statistical code implemented
Hmax = math.log2(q)
print("Hmax: ", Hmax) 


for character, number_of_repetitions in characters.items():
    if character != '\n':   
        print(character," : ", number_of_repetitions)
    else:
        print("\\n : ", number_of_repetitions)
 
for character, frequency in character_frequency.items():
    if character != '\n':   
        print(character," : ", frequency)
    else:
        print("\\n : ", frequency)
 



# calculate the entropy of the source without the memory

H0 = 0
for character, frequency in character_frequency.items():
    H0 += frequency * math.log2(frequency)

H0 = -H0
print("H0: ", H0) 






