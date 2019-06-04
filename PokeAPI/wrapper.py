import requests

class pokemon(object):

    def __init__(self, name):
        self.name = name
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
        self.response = requests.get(url)
        self.poke_stats = self.response.json()['stats']
        self.poke_stats_sorted= {}

        count = 0
        for stats in self.poke_stats:
            self.poke_stats_sorted[stats['stat']['name']] = stats['base_stat']

        self.poke_stat_atck = self.poke_stats_sorted['attack']
        self.poke_stat_def = self.poke_stats_sorted['defense']
        self.poke_stat_spd = self.poke_stats_sorted['speed']
        self.poke_stat_hp = self.poke_stats_sorted['hp']
        self.poke_stat_spe_atck = self.poke_stats_sorted['special-attack']
        self.poke_stat_spe_def = self.poke_stats_sorted['special-defense']
        self.pokeTypes = []
        for pokeType in self.response.json()['types']:
            self.pokeTypes.append(pokeType['type']['name'])
        self.image = self.response.json()['sprites']['front_default']
