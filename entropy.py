import math as math
import os

if __name__ == "__main__":
    
    file_to_be_analysed = "Na_Drini_cuprija.txt"
    zipped_file = "Na_Drini_cuprija.zip"
    
    txt_file_size = os.stat(file_to_be_analysed).st_size
    print('Text file size in bytes is',txt_file_size)
    zipped_file_size = os.stat(zipped_file).st_size
    print('Compressed file size in bytes is',zipped_file_size)
    
    characters = {}
    character_frequency = {}
    doublets = {}
    doublet_frequency = {}
    number_of_characters = 0
    
    
    with open(file_to_be_analysed, encoding='utf-8') as f:
        file_content = f.read()
        
        # iterate througt the file to find number of occurence of 
        # a particular character
        for character in file_content:
            number_of_characters += 1
            if str(character) in characters:
                characters[str(character)] += 1
            else:
                characters[str(character)] = 1 
    
        # make variation with repetition of all characters 
        for character_first, _ in characters.items():
            for character_second, _ in characters.items():
                doublets[character_first + character_second] = 0
    
        # iterate througt the file to find number of occurence of 
        # a particular character doublet
        first = file_content[0]
        for char in file_content[1:]:
            second = char
            doublets[str(first) + str(second)] += 1
            first = second
        
    # calculate frequency of character X occurence - probability: P(X)
    for character, number_of_repetitions in characters.items():
        character_frequency[character] = number_of_repetitions / number_of_characters
    
    # calculate frequency of character doublet XY occurence - probability: P(Y|X)
    first_character_doublete_number = {}
    for char, _ in characters.items():
        total_first_char = 0        
        for doublet, occ_of_doublet in doublets.items():
            if doublet[0] == char:
                total_first_char += occ_of_doublet
        first_character_doublete_number[char] = total_first_char
    
    for doublet, occ_of_doublet in doublets.items():
        doublet_frequency[doublet] = doublets[doublet] / first_character_doublete_number[doublet[0]]
    
    q = len(characters)
    print("Number of different elements is ", q)
    
    
    # calculate the maximal entropy of the source without any statistical code implemented
    Hmax = math.log2(q)
    print("Hmax = ", round(Hmax,2)) 
    
    
    
    # calculate the entropy of the source without the memory
    
    H0 = 0
    for character, frequency in character_frequency.items():
        H0 += frequency * math.log2(frequency)
    
    H0 = -H0
    print("H0 = ", round(H0,2)) 
    
    # calcuate the entropy of the source with memory m = 1 
    
    H1 = 0
    for si, _ in characters.items(): # i
        inner_sum = 0
        for sj, _ in characters.items(): # j
            if doublet_frequency[si + sj] != 0:
                inner_sum +=  - doublet_frequency[si + sj] * math.log2((doublet_frequency[si + sj])) 
        H1 += character_frequency[si] * inner_sum
            
    print("H1 = ", round(H1,2))
            
            
            
    # calculate the maxilam compresion level
    rho_max = txt_file_size / zipped_file_size
    # entropy that can be reached in infinite process
    
    H = math.log2(q) / rho_max
    print("H = ", round(H,2)) 
            
