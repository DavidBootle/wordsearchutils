name = "wordsearchutils"

class Character (object):
  def __init__(self, char, coords, word=None):
    self.char = char
    self.coords = coords
    if word != None:
      self.words = []
    else:
      self.words = [word]
  
  def __str__(self):
    return self.char

class WordSearch (object):
  def __init__(self, word_search_matrix, word_list = [], ignore_spaces = True, case_sensitive = False):
    # generate character matrix

    # removes spaces from words if ignore_spaces is true
    if ignore_spaces:
      temp_word_list = []
      for word in word_list:
        temp_word_list.append(word.replace(" ",""))
      self.word_list = temp_word_list
    else:
      self.word_list = word_list

    # if case_sensitive is false, changes all words to lower case
    if not case_sensitive:
      temp_word_list = []
      for word in self.word_list:
        if not case_sensitive:
          temp_word_list.append(str.lower(word))
      self.word_list = temp_word_list

    # generates the word search matrix
    self.word_obj_list = []
    self.matrix = []
    y = 0
    while y < len(word_search_matrix):
      self.matrix.append([])
      row = word_search_matrix[y]
      x = 0
      # transforms the original matrix into a matrix of wordsearchutils.Character objects
      while x < len(row):
        if type(row[x]) != Character:
          self.matrix[y].append(Character(row[x], (x,y)))
        else:
          self.matrix[y].append(row[x])
        x += 1
      y += 1

    # assigns directional matrices
    self.directional_matrices = {
      "right" : self.matrix,
      "left" : WordSearch.rotate_180(self.matrix),
      "down" : WordSearch.rotate_90(self.matrix),
      "up" : WordSearch.rotate_270(self.matrix)
    }
    self.directional_matrices["diagonal_right"] = WordSearch.get_diagonal(self.matrix)
    self.directional_matrices["diagonal_left"] = WordSearch.get_diagonal(self.directional_matrices["left"])
    self.directional_matrices["diagonal_down"] = WordSearch.get_diagonal(self.directional_matrices["down"])
    self.directional_matrices["diagonal_up"] = WordSearch.get_diagonal(self.directional_matrices["up"])

  # prints one of the matrices
  def print_chars(self, direction = "right"):
    for row in self.directional_matrices[direction]:
      for character in row:
        print(character.char, end="")
      print()
  
  def print_coords(self, direction = "right"):
    for row in self.directional_matrices[direction]:
      for character in row:
        print(character.coords, end="")
      print()
  
  def print_all_matrices(self):
    for matrix in self.directional_matrices:
      for row in self.directional_matrices[matrix]:
        for char in row:
          print(char.char, end="")
        print()
      print()
      for row in self.directional_matrices[matrix]:
        for char in row:
          print(char.coords, end="")
        print()
      print(end="\n\n")
  
  def print_word_obj_list(self):
    for word_obj in self.word_obj_list:
      word_obj.print_info()
      print()
  
  def parse(self):
    for word in self.word_list:
      for matrix in self.directional_matrices:
        for row in self.directional_matrices[matrix]:
          temp_string = ""
          for char in row:
            temp_string += char.char
          if temp_string.find(word) != -1:
            index = temp_string.find(word)
            if temp_string[index:index+len(word)] == word:
              end_index = index + len(word)
              temp_list = []
              i = index
              while i < end_index:
                temp_list.append(row[i])
                i += 1
              word_obj = Word(word, temp_list)
              for word_obj_2 in self.word_obj_list:
                if Word.equal(word_obj, word_obj_2):
                  self.word_obj_list.remove(word_obj_2)
              self.word_obj_list.append(word_obj)
  
  def __str__(self):
    temp_matrix = []
    index = 0
    for row in self.matrix:
      temp_matrix.append([])
      for char in row:
        temp_matrix[index].append(char.char)
      index += 1
    return temp_matrix
  
  '''Flip horizantal has been replaced with rotate_180 as it is accurate.'''
  def flip_horizantal(word_search_matrix):
    temp_matrix = []
    row = 0
    while row < len(word_search_matrix):
      temp_matrix.append([])
      char_index = len(word_search_matrix[row]) - 1
      while char_index > -1:
        temp_matrix[row].append(word_search_matrix[row][char_index])
        char_index -= 1
      row += 1
    return temp_matrix

  def rotate_90(word_search_matrix):
    temp_matrix = []
    for char in word_search_matrix[0]:
      temp_matrix.append([])
    for row in word_search_matrix:
      i = 0
      for char in row:
        temp_matrix[i].append(char)
        i += 1
    word_search_matrix = temp_matrix
    for row in word_search_matrix:
      row.reverse()
    return word_search_matrix

  def rotate_270(word_search_matrix):
    temp_matrix = []
    for char in word_search_matrix[0]:
      temp_matrix.append([])
    for row in word_search_matrix:
      i = len(word_search_matrix[0]) - 1
      for char in row:
        temp_matrix[i].append(char)
        i -= 1
    word_search_matrix = temp_matrix
    return word_search_matrix
  
  def rotate_180(word_search_matrix):
    rotate1 = WordSearch.rotate_90(word_search_matrix)
    rotate2 = WordSearch.rotate_90(rotate1)
    return rotate2

  def get_diagonal(word_search_matrix):
    diagonal_num = len(word_search_matrix) + len(word_search_matrix[0]) - 1
    temp_matrix = []
    for x in range(diagonal_num):
      temp_matrix.append([])
    parsing = True
    # determines when the row stops
    stop_vertical = -1
    stop_horizantal = len(word_search_matrix[0])
    start_index_vertical = 0
    start_index_horizantal = 0
    char_index_vertical = 0
    char_index_horizantal = 0
    diagonal_row = 0
    while parsing:
      while char_index_vertical > stop_vertical and char_index_horizantal < stop_horizantal:
        temp_matrix[diagonal_row].append(word_search_matrix[char_index_vertical][char_index_horizantal])
        char_index_vertical -= 1
        char_index_horizantal += 1
      # check for end of word search
      diagonal_row += 1
      if diagonal_row >= diagonal_num:
        parsing = False
      # determines whether to add vertical or horizantal index
      if start_index_vertical < (len(word_search_matrix) - 1):
        start_index_vertical += 1
      else:
        start_index_horizantal += 1
      char_index_horizantal = start_index_horizantal
      char_index_vertical = start_index_vertical
    return temp_matrix
      

class Word (object):
  def __init__(self, word, char_list = []):
    self.word = word
    self.char_list = char_list
  
  def add_char(self, char):
    self.char_list.append(char);
    char.words.append(self)
  
  def print_info(self):
    print(self.word)
    for char in self.char_list:
      print(char.coords)
  
  def equal(arg1, arg2):
    if arg1.word == arg2.word and arg1.char_list == arg2.char_list:
      return True
    else:
      return False
  
  def __str__(self):
    return self.word