# =================== IMPORTS =================== #
import json
import os
from time import sleep
import random
from os.path import dirname, join

# Word List Categories: Names, Movies, Animals
# nwl (Names Word List)
nwl = json.loads(open(join(dirname(__file__), '0names.json')).read())
mwl = json.loads(open(join(dirname(__file__), '0movies.json')).read())
awl = json.loads(open(join(dirname(__file__),'0animals.json')).read())

categories = {
  1 : nwl, # names
  2 : mwl, # movies
  3 : awl, # animals  
}
# ================= FUNCTIONS ================= #
# Main Menu
def get_option():
  print('Welcome to Word Guesser!')
  print('======== MENU ========')
  print('1. Singleplayer')
  print('2. Rules')
  print('3. Scoreboard')
  print('4. Exit Game')

# Outputs the scoreboard (win/loss, games played, etc.)
def scoreboard(wins: int, losses: int):
  print('====== Scoreboard ======')
  print(f'Games Played: {wins+losses}')
  print(f'Wins: {wins}')
  print(f'Losses: {losses}')
  if wins+losses > 0:
    print(f'Win Percentage: {round(wins/(wins+losses), 2)}')
  else:
    print(f'Win Percentage: 0.00%')

# Outputs the rules of the game
def rulebook():
  print('                        Rules of Hangman! ')
  print('1. You will be given a word and you have to try and guess the word')
  print('2. If you guess 7 wrong, the game will end and you will lose :(')
  print('3. You can either guess a letter, or guess the whole word')
  print('   If there are multiple words, you must guess all words (guessing one of the multiple words will not work)')
  print('4. Have Fun! :)')

# Creating a Loading Screen for the game
def loading_scr():
  # Define the length of the loading bar
  bar_length = 5
  # Creating a loop for outputting the loading bar
  for i in range(bar_length + 1):
    # Create the loading bar with the dashes
    loading_bar = "Loading: ||" + "-" * i + " " * (bar_length - i) + "||"
    # Output
    print(loading_bar)
    sleep(0.15)
    clear()
  
# Clearing the loading screen
def clear():
  if os.name == 'nt': 
    os.system('cls')
  else: 
    os.system('clear')

# Listing Categories for users
def category_options():
  print('====== Category Options ======')
  print('1. Celebrity Names\n2. Movie Names\n3. Animals')

# Generating a random word from category selected
def get_word(category: list) -> list:
  # Using the master list to find words and returning a random one
  master_list = categories[category]
  return master_list[random.randint(0,len(master_list))].lower()

# Fix output in this function to something similar to your loading function
def game_start():
  for i in range(1,4):
    print(f'Game will begin in {i}')
    clear()

# Creates a dictionary to mark the index of every letter in the word ( ex. WOOD = {'W':[0], 'O':[1,2], 'D:'[3]} )
def make_dictionary(word: str) -> dict:
  dictionary = {}
  for i in range(len(word)):
    if word[i] not in dictionary:
      dictionary[word[i]] = [i]
    else:
      dictionary[word[i]] += [i]

  return dictionary

# Making the word hidden by replacing it with asterisks
def make_hidden_word(word):
  hidden = []
  for i in word:
    # Making sure that spaces are not included in the guessed letters
    if i != ' ':
      hidden.append('*')
    else:
      hidden.append(' ')
  return hidden

# Checks if the guessed letter/word is correct
def check_letter(dictionary: dict, word: str, letter: str, hidden: list) -> bool:
  
  # If whole word is guessed
  if letter == word:
    for i in range(len(word)):
      hidden[i] = word[i]
    return True
  
  # If a letter in the word is guessed
  elif letter in word:
    for i in (dictionary[letter]):
      hidden[i] = letter
    return True
  
  else:
    return False
  
# ================= VISUALS ================= #
#indexes 0 - 7: User will have 7 tries
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
  ========
  ''', '''
  +---+
  |   |
  o   |
      |
      |
      |
  ========
  ''', '''
  +---+
  |   |
  o   |
  |   |
      |
      |
  ========                
    ''', '''
  +---+
  |   |
  o   |
 \|   |
      |
      |
  ========                
    ''', '''
  +---+
  |   |
  o   |
 \|/  |
      |
      |
  ========                
    ''', '''
  +---+
  |   |
  o   |
 \|/  |
  |   |
      |
  ========                
    ''', '''
  +---+
  |   |
  o   |
 \|/  |
  |   |
 /    |
  ========                
    ''', '''
  +---+
  |   |
  o   |
 \|/  |
  |   |
 / \  |
  ========                
    ''']

# =================== MAIN FUNCTION ============= #
clear()
wins = 0
losses = 0

while True: 
  try:
    get_option()
    option = None
    while option not in [1,2,3,4]:
      option = int(input('Enter an option (1-4): '))
      loading_scr()

    match option:
      case 1:
        try:
          category_options()
          category = None
          while category not in [1,2,3]: 
            category = int(input('Enter a options (1-3): '))
          loading_scr()
        except: 
          print('Enter only the options 1, 2 or 3')
          sleep(1)
          loading_scr()

# ============== Singleplayer Game ============== #
        # Constants
        word = get_word(category)
        dictionary = make_dictionary(word)
        hidden = make_hidden_word(word)
        guessed = set()
        wrong = 0
        game = 0
        guessed_letter = None
        print(word)

        game_start()
        
        print(f'Category: {category}')

        # Output to the user the length of the word
        print(f'Your word is {len(word)} letters long. Good Luck!')

        # Using a loop to allow user multiple guesses for a letter
        while ''.join(hidden) != word and wrong != 7: 
          if game != 0:
            print(f'Category: {category}')
            print(stages[wrong])
          
          game += 1
          
          print(f"\nGuessed Letters: {', '.join(list(guessed))}")
          guessed_letter = input(f"Guess a letter: {' '.join(hidden)} > ").lower()

          # If letter is guessed twice
          if guessed_letter in guessed:
            print(stages[wrong])
            print(f'Hey! You already guessed "{guessed_letter}"!')

          # If letter guessed is wrong
          elif check_letter(dictionary, word, guessed_letter, hidden) == False:
            if guessed_letter not in guessed:
              wrong += 1
              guessed.add(guessed_letter)
            print(f'Too bad! {guessed_letter} is not in the word!')

          # If Word is guessed correctly
          elif ''.join(hidden) == word:
            print('You guessed the correct word!')

          # If letter is guessed properly
          else:
            print('You guessed the correct letter!')
            guessed.add(guessed_letter)

          sleep(1.5)
          clear()

        # If the whole word is guessed properly    
        if ''.join(hidden) == word:
          print("Congradulations, you guessed the word! You Win :)")
          sleep(1.5)
          loading_scr()
          wins += 1
        # Outputs message if user lost
        else:
          print('\nSorry, You Lose :(')
          print(f'The word was: {word}')
          print('Better Luck Next Time\n')
          sleep(1.5)
          loading_scr()
          losses += 1

      case 2:
        rulebook()
        enter = input('Press enter to go back...')
        loading_scr()

      case 3: 
        scoreboard(wins, losses)
        enter = input('Press enter to go back...')
        loading_scr()

      case 4:
        print('Exiting Program')
        sleep(1)
        loading_scr()
        print('Exited Program')
        break

  except:
    print('Enter only the options 1, 2, 3 or 4')
