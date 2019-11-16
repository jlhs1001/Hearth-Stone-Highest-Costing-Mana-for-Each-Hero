import requests

url = "https://raw.githubusercontent.com/rfilmyer/hearthstone-db/master/cards/all-cards.json"
r = requests.get(url)
#---------------------------------
data = r.json()
#---------------------------------
hero_names = ['priest', 'warrior', 'mage', 'shaman', 'paladin', 'hunter', 'warlock', 'rogue', 'druid']
for hero in hero_names:
    high_cost = 0
    high_cost_name = ''
    h_name = ''
    for d in data['cards']:
        if d['hero'] == hero:
            cost = d['mana']
            c_name = d['name']
            if cost and cost > high_cost:
                high_cost = cost
                high_cost_name = c_name
                h_name = d['hero']
    print(h_name, high_cost_name, high_cost)
#----------------------------------