Requires pygame

Files and purposes:

  main.py: contains playSorry method, also handles graphics

  deck.py: create Deck class to handle pulling random cards from deck, should have init and drawCard
  
  board.py: create Board class, should keep track of whose turn it is, squares
  
  player.py: create a Player class, each player should have init and makeMove
  
  human.py: Implements Human class which inherits from Player
  
  bot.py: Implements Bot class which inherits from Player

Misc:

Sorry! is represented internally with key 0

Off spaces "Start" and "End1", "End2", "End3", "End4", "End5"
0 is red start, squares are mod 60
