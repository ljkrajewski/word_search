# word_search
Searches a dictionary of words to find one that meets a given criteria.

The criteria of the word "description":
- the length of the "description" is the length of the word,
- any letters in the "description" are in the word and in they same location of the word as it is in the "description,"
- unknown letters in the "description" are represented by numbers,
- the same number in a "description" is the same letter in the word.

Examples:
- "123" could be translated to "the", "and", "two", but not to "all", or "then".
- "1223" could be translated to "look" but not "ball" or "then" or "the".
- "34ll5" could be translated to "balls", "bills", "hills", "halls", "falls", etc.
