# Serbian-language-entropy

Serbian Language entropy is calculated by analzsing large text written in Serbian Latin. 

Maximal entropy ```H<sub>max</sub>``` is calculated with the assumption that every symbol has the same occurrence probability.

Entropy ot the text ```H<sub>0</sub>``` is calculated as standard entropy of the source without memory. The probability of a particular symbol is calculates as ratio of number of its occurrences and total number of symbols in the text.

Entropy ot the text ```H<sub>1</sub>``` is calculated as standard entropy of the source with first memory order. The probability of a particular symbol is calculates as ratio of number of its occurrences and total number of symbols in the text. The conditional probability of a pair of symbols is calculates as a ratio of number of its occurrences and total number of pairs with the same first element of the searched pair.

