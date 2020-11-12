import random

input1 = input("Welcome to Bottega Slots! '777' is worth $2, 'cherries' \nis worth $4, and 'diamonds' is worth $12! \nIf 'bomb' shows, you lose your money! It costs $5 to spin. \nWould you like to play? (y = yes, n = no)\nEnter here:")

wallet = 100
while input1 == 'y':
  main_container = []
  result = []
  winnings = 0
  
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
    

  else:
    wallet = wallet - 5 + winnings
    print(result)
    print(f"Congratulations! You win ${winnings}! You now have ${wallet} in your wallet.")
    main_container.remove(random_selection)

  input1 = input("\nWould you like to play again? (y = yes, n = no)\nEnter here:")
  if input1 == 'n':
    print("Thank you for playing!")


