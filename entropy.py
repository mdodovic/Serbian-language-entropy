import numpy as np
import math as math
text_file = open("file.txt","r");

characters = {}
for line in text_file:
    for character in line:
        if str(character) in characters:
            characters[str(character)] += 1
        else:
            characters[str(character)] = 1 
            
text_file.close()

q = len(characters)
print("Number of different elements: ", q)



character_frequency = {}
for character, number_of_repetitions in characters.items():
    character_frequency[character] = number_of_repetitions / q 

for character, number_of_repetitions in characters.items():
    print(character,"(",str(type(character)),") : ", number_of_repetitions)


for character, frequency in character_frequency.items():
    print(character,"(",str(type(character)),") : ", frequency)

H0 = 0

for character, frequency in character_frequency.items():
    H0 += frequency * math.log2(frequency)

H0 = -H0

Hmax = math.log2(q)
print("Hmax: ", Hmax) 

print("H0: ", H0) 






