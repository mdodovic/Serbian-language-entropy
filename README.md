# Serbian-language-entropy

Serbian Language entropy is calculated by analyzing large text Na Drini Ćuprija written in Serbian Latin. 

Maximal entropy H<sub>max</sub> is calculated with the assumption that every symbol has the same occurrence probability.

The Entropy H<sub>0</sub> of the text is calculated as the standard entropy of the source without memory. The probability of a particular symbol is calculated as the ratio of the number of its occurrences and the total number of symbols in the text.

The Entropy H<sub>1</sub> of the text is calculated as standard entropy of the source with first memory order. The probability of a particular symbol is calculated as the ratio of the number of its occurrences and the total number of symbols in the text. The conditional probability of a pair of symbols is calculated as a ratio of the number of occurrences and the total number of pairs with the same first element of the searched pair.

