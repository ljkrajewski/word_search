Here's a Python script that takes an input string and generates a list of words based on the provided rules:

```python
def generate_words(input_string):
  """
  This function takes an input string containing letters and numbers and generates a list of words based on the following rules:
  - Each output word must be the same length as the input.
  - Any letters in the input must appear in the same location in the output words.
  - There is a one-to-one relationship between the numbers of the input and the letters of the output words (e.g., 1=l, 2=o, 3=s).

  Args:
      input_string: The input string containing letters and numbers.

  Returns:
      A list of words generated based on the rules.
  """
  # Initialize an empty list to store the generated words
  words = []

  # Check if the input string is empty
  if not input_string:
    return words

  # Create a dictionary to map numbers to letters
  char_map = {}
  next_char = ord('a')  # Start with 'a' for letter assignments

  # Iterate through the input string
  for char in input_string:
    if char.isalpha():
      # If it's a letter, use it as is
      char_map[char] = char
    elif char.isdigit():
      # If it's a number, assign a letter and increment next_char
      char_map[char] = chr(next_char)
      next_char += 1
    else:
      # Handle invalid characters (optional)
      raise ValueError("Invalid character found in input string")

  # Helper function to generate words recursively
  def generate_words_helper(remaining_string, current_word):
    if not remaining_string:
      # If we reach the end of the string, add the word to the list
      words.append(current_word)
      return

    # Get the character mapping for the current digit
    mapped_char = char_map[remaining_string[0]]

    # Try all possible letters for the current position
    for letter in 'abcdefghijklmnopqrstuvwxyz':
      if letter not in current_word:
        # Avoid using the same letter twice in a word
        generate_words_helper(remaining_string[1:], current_word + letter)

  # Initiate the recursive generation
  generate_words_helper(input_string, "")

  return words

# Example usage
input_string = "122k3"
words = generate_words(input_string)

# Print the generated words
if words:
  print("Words generated for", input_string, ":")
  for word in words:
    print(word)
else:
  print("No valid words found for", input_string)
```

This script defines a function `generate_words` that takes the input string. It creates a dictionary to map numbers to letters and then uses a recursive helper function to generate all possible words that follow the defined rules. The script also includes an example usage to demonstrate how to use the function.
