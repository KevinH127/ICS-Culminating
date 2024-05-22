# =================== IMPORTS =================== #
from GameFiles.game_functions import *
from GameFiles.hangman_stages import *

# ============== SinglePlayer Function ============== #
def singleplayer(category):
  # Constants
  word = get_word(category)
  dictionary = make_dictionary(word)
  hidden = ['*']*len(word)
  guessed = set()
  wrong = 0
  guessed_letter = None

  # Output
  print(f'Your word is {len(word)} letters long. Good Luck!')

  # Using a loop to allow user multiple guesses for a letter
  while ''.join(hidden) != word and wrong != 7: 
  
    guessed_letter = input(f"\nGuess a letter: {' '.join(hidden)} > ").lower()
    
    # If letter is guessed twice
    if guessed_letter in guessed:
      print(stages[wrong])
      print(f'Hey! You already guessed {guessed_letter} correctly!')
    
    # If letter guessed is wrong
    elif check_letter(dictionary, word, guessed_letter, hidden) == False:
      if guessed_letter not in guessed:
        wrong += 1
      print(stages[wrong])
      print(f'Too bad! {guessed_letter} is not in the word!')
    
    # If letter is guessed properly
    else:
      print(stages[wrong])
      guessed.add(guessed_letter)
    

  # If the whole word is guessed properly    
  if ''.join(hidden) == word:
    print(word)
    print("Congradulations, you guessed the word!")
  
  # Outputs message if user lost
  else:
    loss(word)