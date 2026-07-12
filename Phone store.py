import random

laptop = {'brand':'sumsung','model':'A50','battery life':'11h' }

print('welcome to joshus phone store ')
print('we have a huge invetory of phones')
print('please indicate your prefrence of specs')
print()

def append_s(og):
    return og + 's'

print()

phone_list = []

specs = ['brand', 'model', 'batery life', 'chip set', 'RAM', 'fps', 'price']

specs_new = list(map(append_s, specs))
master_dict = dict.fromkeys(specs_new)



master_dict['Brands'] =  ['sumsung', 'apple', 'xsoumi', 'redmagic', 'itel']
master_dict['Models'] = ['AAA', 'BBB', 'CCC']
master_dict['CPUs'] = ['snapdragon8', 'A8', 'Dimencity4550']
master_dict['Speeds'] = ['2 GHz', '3 GHz', '3.15 GHz', '3.8 GHz']
master_dict['RAMs'] = [ '2 GB', '4 GB', '8 GB', '16 GB']
master_dict['Storages'] = [ '128 GB', '256 GB', '512 GB', '1024 GB']
master_dict['Screensizes'] = [ '6.1 in', '6.5 in', '5 in', '7 in']
master_dict['Prices'] = ['zm 9000', 'zm 27000', 'zm 12000']

for n_phone in range(30):
  new_phone = dict.fromkeys(specs)
  for kk in new_phone:
    new_phone[kk] = random.choice(master_dict[kk+'s'])
  phone_list.append(new_phone)  

user_choice = dict.fromkeys(specs)
for kk in specs:
  user_choice[kk] = input('Any preference for ' + kk + ' (Enter none for no preference)'+'\n')
  

query = ''

for kk in user_choice:
  if user_choice[kk].lower() == 'none':
    pass
  else:
    query = query + 'phone[' + '\'' + kk + '\'] == ' + '\'' + user_choice[kk] + '\' and '

print(query)


input()

query = query[0:-4:1]



if query != '':
  selected = [phone for phone in phone_list if eval(query)]
else:
  selected = [phone for phone in phone_list]
  


print(len(selected), 'phone met your preference.')

characters = 0
for kk in specs:
  print(kk, end = '')
  characters = len(kk)
  print((12 - characters)*' ', end = '')
print()

characters = 0

for phone in selected:
  for kk in phone:
    print(phone[kk],  end = '')
    characters = len(phone[kk])
    print((12 - characters)*' ', end = '')
  print()
  

'''

for kk in phone:
  print(kk, end = '\t\t')

print()

for jj in range(len(phone_list)):
  for kk in laptop:
    if kk in units:
      print(str(phone_list[jj][kk]) + ' ' + units[kk], end='\t\t')
    else:
      print(str(phone_list[jj][kk]), end='\t\t')
  print()


user_choice_phone = dict.fromkeys(keys_list)

user_choice_brand = input('Your preferred brand')

user_choice_phone['brand'] = user_choice_brand

user_choice_batery_life = input('Your preferred batery life')

user_choice_phone['CPU'] = user_choice_batery_life

for kk in phone:
  print(kk, end = '\t\t')

print()

for jj in range(len(phone_list)):
  for kk in laptop:
    if user_choice_phone[kk] == phone_list[jj][kk] or user_choice_phone[kk] == 'Any':
      if kk in units:
         print(str(phone_list[jj][kk]) + ' ' + units[kk], end='\t\t')
      else:
        print(str(phone_list[jj][kk]), end='\t\t')
    else:
      break
  print()



'''
   


#test
