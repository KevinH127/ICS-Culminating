# =================== IMPORTS =================== #
from GameFiles.game_functions import *
from GameFiles.gamemodes import *
from GameFiles.hangman_stages import *

clear()

try:
  get_option()
  option = None
  while option not in [1,2]:
    option = int(input('Enter an option (1-2): '))
    sleep(1)
    clear()
  
  match option:
    case 1:
      try:
        category_options()
        category = None
        while category not in [1,2,3]: 
          category = int(input('Enter a options (1-3): '))
          sleep(1)
          clear()
      except: 
        print('Enter only the options 1, 2 or 3')
        sleep(1)
        clear()
      
      singleplayer(category)
    
    case 2:
      print('Exiting Program')
      sleep(1)
      clear()
      print('Exited Program')
      exit()


except:
  print('Enter only the options 1 or 2')
  sleep(1)
  clear()
