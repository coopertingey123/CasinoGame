import random


def slot_machine():
  winnings = 0
  wallet = 100
  main_container = []
  result = []
  for i in range(4): 
    for j in range(4): 
        for k in range(4):
          for l in range(4):
              main_container.append([i, j, k, l])
  random_selection = random.choice(main_container)
  for num in random_selection:
    if num == 0:
      result.append('bomb')
      winnings = 0
    elif num == 1:
      result.append('777')
      winnings = winnings + 2
    elif num == 2:
      result.append('cherries')
      winnings = winnings + 4
    elif num == 3:
      result.append('diamonds')
      winnings = winnings + 12
  if 'bomb' in result:
    wallet = wallet - 5
    print(result)
    print("Sorry, better luck next time!")
    print(f"You now have ${wallet} in your wallet.")
    prompt = input("\nWould you like to play again?")
    if prompt == 'y':
      slot_machine()
    elif prompt == 'n':
      return print("Thank you for playing!")
  else:
    wallet = wallet - 5
    print(result)
    print(f"Congratulations! You win ${winnings}! You now have ${winnings + wallet} in your wallet.")
    prompt = input("\nWould you like to play again? (Enter y for yes and n for no)")
    if prompt == 'y':
      slot_machine()
    elif prompt == 'n':
      print("Thank you for playing!")
      
  main_container.remove(random_selection)
    
slot_machine()
          