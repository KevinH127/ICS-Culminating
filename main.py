# =================== IMPORTS =================== #
from GameFiles.game_functions import *
from GameFiles.gamemodes import *
from GameFiles.hangman_stages import *

clear()
wins = 0
losses = 0

while True: 
  try:
    get_option()
    option = None
    while option not in [1,2, 3]:
      option = int(input('Enter an option (1-3): '))
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
        scoreboard(wins, losses)
        enter = input('Press enter to go back...')

      case 3:
        print('Exiting Program')
        sleep(1)
        clear()
        print('Exited Program')
        break


  except:
    print('Enter only the options 1, 2 or 3')
    sleep(1)
    clear()
