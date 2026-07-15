import csv
import random

with open('dino.csv', mode ='r') as file:
  csvFile = csv.DictReader(file)
  all_cards = list(csvFile)

print("Welcome to the Top Trumps, dinosour editiom")
print('Make your choices wisely and try to win all the cards')
print('Click Enter to begin')

input()

def disp_card(card):

  max_chars = 0
  
  for keys in card:
    if len(keys) > max_chars:
      max_chars = len(keys)
  
  for keys in card:
    print(keys, (max_chars-len(keys))*' ', ': ', card[keys])
  
def det_winner(m1, m2, order = 1):
  
  dct = {'player': m1, 'computer': m2}
  v = list(dct.values())
  k = list(dct.keys())

  if m1 == m2:
    return 'draw'
  else:
    if order == 1:
      return k[v.index(max(v))]
    else:
      return k[v.index(min(v))]
    
random.shuffle(all_cards)

comp_cards = all_cards[0::2]
p_cards = all_cards[1::2]
t_cards = []
game_over = False
chance = 'player'

relevant_keys = list(all_cards[0].keys())
relevant_keys = relevant_keys[2::]

mapping_dict = {}

for key in relevant_keys:
  mapping_dict[key[0]] = key

input()

while not game_over:

  print('player cards: ', len(p_cards), 'computer cards: ', len(comp_cards), 'table_cards: ', len(t_cards))
  
  player = p_cards.pop(0)
  comput = comp_cards.pop(0)

  t_cards.append(player)
  t_cards.append(comput)

  print()
  print(f'It is now {chance}\'s chance')
  print()

  print('Your (Player) card is ')
  disp_card(player)
  print()

  if chance == 'player':
    chosen_key = input('What is your choice?')
    chance = 'computer'    

  else:
    chosen_key = random.choice(list(mapping_dict.keys()))
    chance = 'player'

  key_requested = mapping_dict[chosen_key]
  value_player = player[key_requested]
  value_comput = comput[key_requested]
  
  print('Key of interest is ', key_requested)

  if chosen_key in ['H','F', 'B']:
    winner = det_winner(float(value_player), float(value_comput)); 
  else:
    winner = det_winner(float(value_player), float(value_comput), 0); 
    
  print('Player ', key_requested, 'is', value_player)
  print('Computer ', key_requested, 'is', value_comput)
  print()
  print('Winner is ... ', winner)
  input()

  if winner == 'player':
    p_cards.extend(t_cards)
    t_cards.clear()
  elif winner == 'computer':
    comp_cards.extend(t_cards)
    t_cards.clear()

  if len(p_cards) == 0:
    print('Computer Won')
    game_over = True
  elif len(comp_cards) == 0:
    print('Player Won')
    game_over = True