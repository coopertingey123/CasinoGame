# casino slot machine

# 4 slots, 4 options (7, cherries, bomb, diamonds,)

#cost: 3$, winnings if:
# contains anybomb: lose 3$
# +$2 for every 7
# +4$ for every cherry
# +$10 for every diamond
# +$100 all of one
# I need to create a container that holds all 256 possible combinations of the slot machine
# From there, I need to pick one out of the 256, so that that combination cannot be  used again until it all starts over and the 256 refreshes
# Do the math to make the house always profit from those 256 results

import random




       
                    

slot_options = {
  1: {'bomb': 'Better luck next time!'},
  2: {'777': 'Add $2'},
  3: {'cherries': 'Add $4'},
  4: {'diamonds': 'Add $12'}
}


print(slot_machine())

import random

winnings = 0
main_container = []
result = []
wallet = 100
def slot_machine():
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
      print(result)
      print("Sorry, better luck next time!")
      print(f"You now have ${wallet} in your wallet.")
    else:
      print(result)
      print(f"Congratulations! You win ${winnings}! You now have ${winnings + wallet} in your wallet.")
    return 


       
                      
slot_machine()