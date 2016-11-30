pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold
def special_pirates(pirate_list):
    spec_pirates = []
    for i in range(len(pirate_list)):
        if pirate_list[i].get('has_wooden_leg') == True and pirate_list[i].get('gold') > 15:
            spec_pirates.append(pirate_list[i]['Name'])
    return spec_pirates

print (special_pirates(pirates))
