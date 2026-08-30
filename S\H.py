import csv

print("Welcome to the Sports Heros")
print('We are going to do some analysis on Wimbledon and French Open Men\'s singles champions')
print('see the file analysis.dat for the results')
def print_line(report_line):
  fn = 'analysis.dat'
  
  with open(fn, mode ='a') as file:
    file.write(report_line)

def p_ta(table):
  
  fn = 'analysis.dat'
  with open(fn, mode ='a') as file:
    all_keys = list(table[0].keys())
    keys_line = ''
    for key in all_keys:
      keys_line = keys_line + key + (20 - len(key))*' '    
    file.write(keys_line + '\n')
    for data in table:
      values_line = ''
      for values in data.values():
        values_line = values_line + str(values) + (20-len(str(values)))*' '

      file.write(values_line + '\n')

def initialize():
  filename = 'analysis.dat'

  with open(filename, mode ='w') as file:
    file.write('Analysis Results \n')

def p_set(w_set):

  filename = 'analysis.dat'

  with open(filename, mode ='a') as file:
    for winner in w_set:
       file.write(winner + ' , ')
    file.write('\n\n')



def rcsvd(tournament_name):
  fn = tournament_name + '.csv'
  
  with open(fn, mode ='r') as file:
    csvFile = csv.DictReader(file)
    t_data = list(csvFile)

  return t_data

def analyze(tname, tdata):
  
  winners_list = []
  
  for winner in tdata:
    winners_list.append(winner['Champion'])

  winners_set = set(winners_list)

  print_line('Reporting for ' + tname + '\n' )
  print_line('Total Winners : ' + str(len(winners_list)) + '\n')
  print_line('Unique Winners : ' + str(len(winners_set)) + '\n')

  w_i_l = []  
  for player in winners_set:
    
    p_info = {}
    selected = [chosen for chosen in tdata if chosen['Champion'] == player]
    
    p_info['Name'] = player
    p_info['Country'] = selected[0]['Country']
    p_info['Times Won'] = len(selected)
    p_info['Years Won'] = []
    for kk in selected:
      p_info['Years Won'].append(kk['Year'])

    w_i_l.append(p_info)

  p_ta(w_i_l)

  mto_winners_set = set()

  for player in winners_set:
    mto_winners_set.add(player)

  for player in winners_set:
    selected = [chosen for chosen in w_i_l if chosen['Name'] == player]
    if selected[0]['Times Won'] == 1:
      mto_winners_set.remove(player)
  
  return winners_set, mto_winners_set

def comparative_analysis(w_set1, w_set2):

  winners_eitheror = w_set1 | w_set2
  winners_both = w_set1 & w_set2
  winners_only1 = w_set1 - w_set2
  winners_only2 = w_set2 - w_set1
  winners_onlyone_notboth = w_set1 ^ w_set2

  print_line('Winners (Either/Or): ' + str(len(winners_eitheror)) + '\n')
  print_line('These are: \n')
  p_set(winners_eitheror)
  
  print_line('Winners (Both): ' + str(len(winners_both)) + '\n')
  print_line('These are: \n')
  p_set(winners_both)
  
  print_line('Winners (Only 1, not both): ' + str(len(winners_onlyone_notboth)) + '\n')

  print_line('These are: \n')
  p_set(winners_onlyone_notboth)

  print_line('Winners (Only Wimbledon, not French Open): ' + str(len(winners_only1)) + '\n')
  print_line('These are: \n')
  p_set(winners_only1)

  print_line('Winners (Only French Open, not Wimbledon): ' + str(len(winners_only2)) + '\n')
  print_line('These are: \n')
  p_set(winners_only2)
       
initialize()

w_data = rcsvd('Wimbledon')
f_data = rcsvd('FrenchOpen')

wimbledon_winners, wimbledon_mto_winners = analyze('Wimbledon', w_data)
frenchopen_winners, frenchopen_mto_winners = analyze('French Open', f_data)

comparative_analysis(wimbledon_winners, frenchopen_winners)