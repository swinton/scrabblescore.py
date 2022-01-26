from functools import reduce

def letterscore(letter: str) -> int:
  """
  Return the score for the given letter, return 0 if letter is not in scores
  """
  scores: dict = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
  }
  return scores.get(letter[0].upper(), 0)

def scrabblescore(word: str) -> int:
  """
  Return the scrabblescore for the given word.
  """
  # Good explanation of Python's map function: https://www.freecodecamp.org/news/python-map-explained-with-examples/
  return reduce(lambda total, current: total+current, map(letterscore, word), 0)
