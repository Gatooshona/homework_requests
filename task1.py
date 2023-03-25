import json
import requests


def hero_request():
    heroes_dict = {}
    heroes = []
    result = []
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    data = response.json()
    with open('all_heroes.json', 'w') as file:  
        json.dump(data, file, indent=2)

    for all_list in data:
        if all_list['name'] == 'Hulk' or all_list['name'] == 'Captain America' or all_list['name'] == 'Thanos':
            heroes_dict.setdefault(all_list['name'], all_list['powerstats'])

    for one_hero in heroes_dict.items():
        heroes.append([one_hero[0], one_hero[1]['intelligence']])
        result = max(heroes)

    print(f'Самый умный супергерой: {result[0]}, его интеллект = {result[1]}')


hero_request()
