# casino slot machine

# 4 slots, 4 options (7, cherries, bomb, diamonds,)

#cost: 3$, winnings if:
# contains anybomb: lose 3$
# +$2 for every 7
# +4$ for every cherry
# +$10 for every diamond
# +$100 all of one

options = {
  1: {'bomb': 'Better luck next time!'},
  2: {'777': 'Add $2'},
  3: {'cherries': 'Add $4'},
  4: {'diamonds': 'Add $12'}
}

wallet = 100

# I need to create a container that holds all 256 possible combinations of the slot machine
# From there, I need to pick one out of the 256, so that that combination cannot be  used again until it all starts over and the 256 refreshes
# Do the math to make the house always profit from those 256 results

import random


def slot_machine():

  mini_container = []
  options_list = [1,2,3,4]
  for num in options_list:
    choice = random.choice(options_list)
    mini_container.append(choice)
  return mini_container
  
      

slot_options = {
  1: {'bomb': 'Better luck next time!'},
  2: {'777': 'Add $2'},
  3: {'cherries': 'Add $4'},
  4: {'diamonds': 'Add $12'}
}


print(slot_machine())