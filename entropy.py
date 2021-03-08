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

for character, number_of_repetitions in characters.items():
    print(character," : ", number_of_repetitions)


q = len(characters)
print("Number of different elements: ", q)

Hmax = math.log2(q)
print("Hmax: ", Hmax) 
print("Hmax: ", math.log2(26)) 

print("Hmax: ", math.log2(27)) 

print("Hmax: ", math.log2(32)) 






