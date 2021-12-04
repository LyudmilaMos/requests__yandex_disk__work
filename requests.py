from pprint import pprint

import requests

TOKEN = '2619421814940190'

urls = [
    f'https://superheroapi.com/api/2619421814940190/search/Hulk',
    f'https://superheroapi.com/api/2619421814940190/search/Captain America',
    f'https://superheroapi.com/api/2619421814940190/search/Thanos',
]

def get_url_list(url_list):
    response = (requests.get(url) for url in url_list)
    return response

def parser():
    superhero = []

    for item in get_url_list(urls):

        intelligence = item.json()

        try:

            for powerstat in intelligence['results']:
                superhero.append(
                    {
                        'name': powerstat['name'],
                        'intelligence': powerstat['powerstats']['intelligence'],
                    }
                )

        except KeyError:

            print(f'You will have to check the urls of the link: {urls}')

    intelligence_superhero = 0
    name = ''

    for intelligence_hero in superhero:

        if intelligence_superhero < int(intelligence_hero['intelligence']):
            intelligence_superhero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f'The highest intelligence in {name}, IQ: {intelligence_superhero}.')
    
parser()