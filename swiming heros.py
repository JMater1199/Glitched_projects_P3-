import csv

print("Welcome to Swimming Heros")
print('We are going to do some analysis on 2021 swimming olympic singles')
print('Please see the file analysis.dat for the results')


def print_line(report_line):
  filen = 'analysis.dat'
  
  with open(filen, mode ='a') as file:
    file.write(report_line)

def print_table(table):
  
  
  filen = 'analysis.dat'

  with open(filen, mode ='a') as file:
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

def print_set(winner_set):
  filename = 'analysis.dat'

  with open(filename, mode ='a') as file:
    for swimmers in winner_set:
       file.write(swimmers + ' , ')
    file.write('\n\n')

def readcsvdata(tournament_name):
  filename = tournament_name + '.csv'
 
  with open(filename, mode ='r') as file:
    csvFile = csv.DictReader(file)
    tournament_data = list(csvFile)

  return tournament_data

def analyze(tname, tdata):
  
  swimmers_list = []
  
  for swimmers in tdata:
    swimmers.append(swimmers['Champion'])

  
  swimmers_set = set(swimmers_list)

  print_line('Reporting for ' + tname + '\n' )
  print_line('Total Winners : ' + str(len(swimmers_list)) + '\n')
  print_line('Unique Winners : ' + str(len(swimmers_set)) + '\n')

  winners_info_list = []  
  for player in swimmers_set:
   
    player_info = {}
    selected = [chosen for chosen in tdata if chosen['Champion'] == player]
    
    player_info['Name'] = player
    player_info['Country'] = selected[0]['Country']
    player_info['Times Won'] = len(selected)
    player_info['Years Won'] = []
    for kk in selected:
      player_info['Years Won'].append(kk['Year'])

    winners_info_list.append(player_info)

  print_table(winners_info_list)

  mto_winners_set = set()

  for player in swimmers_set:
    mto_winners_set.add(player)

  for player in swimmers_set:
    selected = [chosen for chosen in winners_info_list if chosen['Name'] == player]
    if selected[0]['Times Won'] == 1:
      mto_winners_set.remove(player)

  return swimmers_set, mto_winners_set




def comparative_analysis(winner_set1, winner_set2):

  winners_eitheror = winner_set1 | winner_set2
  winners_both = winner_set1 & winner_set2
  winners_only1 = winner_set1 - winner_set2
  winners_only2 = winner_set2 - winner_set1
  winners_onlyone_notboth = winner_set1 ^ winner_set2

  print_line('Winners (Either/Or): ' + str(len(winners_eitheror)) + '\n')
  print_line('These are: \n')
  print_set(winners_eitheror)
  
  print_line('Winners (Both): ' + str(len(winners_both)) + '\n')
  print_line('These are: \n')
  print_set(winners_both)
  
  print_line('Winners (Only 1, not both): ' + str(len(winners_onlyone_notboth)) + '\n')

  print_line('These are: \n')
  print_set(winners_onlyone_notboth)

  
  print_line('Winners (Only Wimbledon, not French Open): ' + str(len(winners_only1)) + '\n')
  print_line('These are: \n')
  print_set(winners_only1)

  
  print_line('Winners (Only French Open, not Wimbledon): ' + str(len(winners_only2)) + '\n')
  print_line('These are: \n')
  print_set(winners_only2)
  

      
initialize()

france_data = readcsvdata('swim.csv')
frenchopen_data = readcsvdata('FrenchOpen')

wimbledon_winners, olympics_mto_swimmersers = analyze('Wimbledon', france_data)
frenchopen_winners, frenchopen_mto_swimmersers = analyze('French Open', frenchopen_data)

comparative_analysis(wimbledon_winners, frenchopen_winners)