import random

laptop = {'brand':'Dell', 'Model': 'ABC111', 'Processor': 'Intel Core i5'}


print('Welcome to joshua\s Laptop store.')
print('We have a huge inventory of laptops.')
print('Please indicate your preference of specs.')
print()

def append_s(name):
  return name + 's'

print()

l_list      = []

specs = ['Brand', 'Model', 'CPU', 'Speed', 'RAM', 'Storage', 'Screensize', 'Price']

s_new = list(map(append_s, specs))
m_dict = dict.fromkeys(s_new)

m_dict['Brands'] =  ['WDell', 'WAsus', 'WAcer', 'WLenovo', 'WHP']
m_dict['Models'] = ['AAA', 'BBB', 'CCC']
m_dict['CPUs'] = ['WIntel i5', 'WIntel i7', 'WAMD Ryzen']
m_dict['Speeds'] = ['2 GHz', '3 GHz', '3.15 GHz', '3.8 GHz']
m_dict['RAMs'] = [ '2 GB', '4 GB', '8 GB', '16 GB']
m_dict['Storages'] = [ '128 GB', '256 GB', '512 GB', '1024 GB']
m_dict['Screensizes'] = [ '9 in', '12 in', '14.9 in', '17 in']
m_dict['Prices'] = ['INR 20000', 'INR 30000', 'INR 40000']

for n_laptops in range(60):
  n_laptop = dict.fromkeys(specs)
  for kk in n_laptop:
    n_laptop[kk] = random.choice(m_dict[kk+'s'])
  l_list.append(n_laptop)  
  
u_choice = dict.fromkeys(specs)
for kk in specs:
  u_choice[kk] = input('Any preference for ' + kk + ' (Enter none for no preference)'+'\n')
  
query = ''

for kk in u_choice:
  if u_choice[kk].lower() == 'none':
    pass
  else:
    query = query + 'laptop[' + '\'' + kk + '\'] == ' + '\'' + u_choice[kk] + '\' and '

print(query)

input()

query = query[0:-4:1]

if query != '':
  selected = [laptop for laptop in l_list if eval(query)]
else:
  selected = [laptop for laptop in l_list]
  
print(len(selected), 'laptops met your preference.')

characters = 0
for kk in specs:
  print(kk, end = '')
  characters = len(kk)
  print((12 - characters)*' ', end = '')
print()

characters = 0

for laptop in selected:
  for kk in laptop:
    print(laptop[kk],  end = '')
    characters = len(laptop[kk])
    print((12 - characters)*' ', end = '')
  print()
  
  

'''

for kk in laptop:
  print(kk, end = '\t\t')

print()

for jj in range(len(l_list)):
  for kk in laptop:
    if kk in units:
      print(str(l_list[jj][kk]) + ' ' + units[kk], end='\t\t')
    else:
      print(str(l_list[jj][kk]), end='\t\t')
  print()


u_c_l = dict.fromkeys(keys_list)

u_c_b = input('Your preferred brand (Acer/Asus/HP/Dell/Any')

u_c_l['brand'] = u_c_b

u_c_C = input('Your preferred CPU (Intel i5/Intel i7/AMD/Any')

u_c_l['CPU'] = user_choice_CPU

for kk in laptop:
  print(kk, end = '\t\t')

print()

for jj in range(len(l_list)):
  for kk in laptop:
    if u_c_l[kk] == l_list[jj][kk] or u_c_l[kk] == 'Any':
      if kk in units:
         print(str(l_list[jj][kk]) + ' ' + units[kk], end='\t\t')
      else:
        print(str(l_list[jj][kk]), end='\t\t')
    else:
      break
  print()



'''