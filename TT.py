import csv 
import random as r

with open('dino.csv', mode ='r') as file:
  csvfile = csv.DictReader(file)
  all_card = list(csvfile)

