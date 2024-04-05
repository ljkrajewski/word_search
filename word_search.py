#!/usr/bin/env python3

'''
Prereqs:
- Downloaded dictionary list (example: https://www.mit.edu/~ecprice/wordlist.10000)

Steps:
1. Filter word list by length of input
2. Filter that list by known letters in known locations
'''

### Main routine ###
def main():
  wordlistFile = "/location/of/wordlist.txt"
  user_input = input("Enter a string: ")
  inputLength = len(user_input)
  firstFilterList = firstFilterList(wordlistFile, inputLength)

### Filter_Words_By_Length ###
def filter_words_by_length(filename, length):
  """
  Reads a list of words from a file and filters them by a specific length.

  Args:
      filename: The path to the text file containing the words.
      length: The desired length of the words.

  Returns:
      A list of words with the specified length.
  """
  words = []
  try:
    with open(filename, "r") as file:
      for line in file:
        words.extend(line.strip().split())
  except FileNotFoundError:
    print(f"Error: File not found: {filename}")
    return []
  return [word for word in words if len(word) == length]

## Example usage
#filtered_words = filter_words_by_length("words.txt", 5)
#print(filtered_words)

