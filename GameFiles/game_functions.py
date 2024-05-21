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
def get_option():
  print('Welcome to Word Guesser!')
  print('\tMENU')
  print('1. Singleplayer')
  print('2. Scoreboard')
  print('2. Exit Game')

# Outputs the scoreboard (win/loss, games played, etc.)
def scoreboard(wins: int, losses: int):
  print(f'Games Played: {wins+losses}')
  print(f'Wins: {wins}')
  print(f'Losses: {losses}')
  print(f'Win Percentage: {round(wins/(wins+losses), 2)}
  
# Clearing the loading screen
def clear():
  if os.name == 'nt': 
    os.system('cls')
  else: 
    os.system('clear')
  
  sleep(1)
  
# Listing Categories for users
def category_options():
  print('\tCategory Options')
  print('1. Celebrity Names\n2. Movie Names\n3. Types of Animals')

# Generating a random word from category selected
def get_word(category: list) -> list:
  # Using the master list to find words and returning a random one
  master_list = categories[category]
  return master_list[random.randint(0,len(master_list))]

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

# Checks if the guessed le
def check_letter(dictionary: dict, word: str, letter: str, hidden: list) -> bool:
  if letter in word:
    for i in (dictionary[letter]):
      hidden[i] = letter
    return True
  else:
    return False
  
def loss(word: str) -> None:
  print('\nSorry, You Lose :(')
  print(f'The word was: {word}')
  print('Better Luck Next Time\n')
  sleep(1)
  
def win(word: str) -> None:
  pass


