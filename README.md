# wordsearchutils
A utility package to help with word search solving applications.

This module arose because I wanted to make a program to solve word searches, and needed custom classes in order to do it. I thought I would make my effort available to the general public. Enjoy!

# Reference
## wordsearchutils.WordSearch
The word search class is an object that can be created to represent a word search.
#### Initialization
```python
wordsearchutils.WordSearch(matrix, word_list, ignore_spaces = True, case_sensitive = False)
```
- `matrix`: A list of lists that represents the characters in a word search.
- `word_list`: A list of the words to find in the word search. The word bank.
- `ignore_spaces`: Boolean; whether or not to remove spaces from words when parsing.
- `case_sensitive`: Boolean; whether the word search and words should be case sensitive.

Example: the `matrix` variable of a 3x3 word search
```python
matrix = [
  ['a','b','c'],
  ['d','e','f'],
  ['g','h','i']
]
```
#### Properties
- **`self.word_list`**: A list containing words to be searched. If `ignore_spaces` is True, the words in `self.word_list` will have spaces removed. If `case_sensitive` is not True, the words in `self.word_list` will be lower case.

- **`self.word_obj_list`**: A list containing `wordsearchutils.Word` objects that were found in the word search. This list is empty until the word search is parsed by using `self.parse()`.

- **`self.matrix`**: A matrix representing the original matrix input, made of `wordsearchutils.Character` objects.

- **`self.directional_matrices`**: A dict object that holds all the rotations of the word search.
  - Keys: `right`, `left`, `up`, `down`, `diagonal_right`, `diagonal_left`, `diagonal_up`, `diagonal_down`
  - The `right` key is equivalent to `self.matrix`.

#### Methods
- **`self.print_chars(self, direction = 'right')`**:
Prints one of the matrix directions, right by default, which is equivalent to `self.matrix`. Converting the `WordSearch` object into a string will return the matrix printed by `direction = 'right'`. Intended as a debugging tool.

- **`self.print_coords(self, direction = 'right')`**:
Prints the coordinates of the characters for one of the matrix directions, right by default. Intended as a debugging tool.

- **`self.print_all_matrices(self)`**:
Prints all 8 directional matrices. Intended as a debugging tool.

- **`self.print_word_obj_list(self)`**:
Prints information on each word in the word object list. If ran before `self.parse()`, nothing will be printed.

- **`self.parse(self)`**:
Parses the word search and fills in `self.word_obj_list` with found words.

- **`self.__str__(self)`**:
Returns a matrix of `string` type characters.

- **`WordSearch.flip_horizantal(matrix)`**:
Flips `matrix` around the y axis.

- **`WordSearch.rotate_90(matrix)`**:
Returns a matrix rotated by 90 degrees.

- **`WordSearch.rotate_180(matrix)`**:
Returns a matrix rotated by 90 degrees.

- **`WordSearch.rotate_270(matrix)`**:
Returns a matrix rotated by 270 degrees.

- **`WordSearch.get_diagonal(matrix)`**:
Returns a diagonal matrix.

## wordsearchutils.Character
#### Initialization
```python
wordsearchutils.Character(char, coords, word = None)
```
- `char`: A string of length 1, representing the character that the object represents.
- `coords`: A two-tuple representing the row and column of the character in the original word search.
- `word`: A `wordsearchutils.Word` object that this character belongs to.

#### Properties
- **`self.char`**: A string of length 1. Equals `char` argument in initialization.

- **`self.coords`**: A two-tuple representing the row and column of the character in the original word search. Equals `coords` argument in initialization.

- **`self.words`**: A list of `wordsearchutils.Word` objects that the character is part of. Before parsing the word search this list will be empty unless initialized with `word` not equal to `None`.

## wordsearchutils.Word
#### Initialization
```python
wordsearchutils.Word(word, char_list = [])
```
- `word`: A string object. Contains the word that the object represents.
- `char_list`: A list of `wordsearchutils.Character` objects that the word contains.

#### Properties
- **`self.word`**: A string object. Contains the word that the object represents.

- **`self.char_list`**: A list of `wordsearchutils.Character` objects that the word contains.

#### Methods
- **`self.add_char(self, char)`**:
Adds a character object to `self.char_list`, where `char` is a `wordsearchutils.Character` object.

- **`self.print_info(self)`**:
Prints `word` and `char_list`.

- **`Word.equal(word1, word2)`**:
Returns True if both `Word` objects have the same `word` and the same `char_list`.

- **`self.__str__(self)`**:
Returns `self.word`.

© David Bootle 2019

Protected under CC Attribution 4.0 International
