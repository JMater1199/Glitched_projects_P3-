import random

laptop = {'brand':'sumsung','model':'A50','battery life':'11h' }

print('welcome to joshus phone store ')
print('we have a huge invetory of laptops')
print('please indicate your prefrence of specs')
print()

def append_s(og):
    return og + 's'
s
print()

phone_list = []

specs = ['brand', 'model', 'batery life', 'chip set', 'RAM', 'fps', 'price']

specs_new = list(map(append_s, specs))
master_dict = dict.fromkeys(specs_new)



master_dict['Brand'] = ['Sumsung','Apple','JS','Wibites spetial']
master_dict['model'] = ['A50','17pro','Vict','forever enjoy codding']
master_dict['batery life'] = ['1h','30h','12h','15h']
master_dict['chip set'] = ['snapdragon8 elite','Razon5661 elite','A19 pro','mediatek dimention 9500']
master_dict['RAM'] = ['32GB','100GB','89GB','69GB']
master_dict['fps'] = ['60','120','70','39']
master_dict['price'] = ['11000k','1500k','9000k','24000k']
print()

for n in range(100):
    new_phone = dict.fromkeys(specs)
    for kk in new_phone:
        new_phone[kk] = random.choice(master_dict[kk+'s'])
    phone_list.apennd


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
   


