URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',
    'summoner_id': 'v{version}/summoner/{summonerids}',
    'summoner_masteries': 'v{version}/summoner/{summonerids}/masteries',
    'game': 'v{version}/game/by-summoner/{summonerids}/recent'
}

API_VERSIONS = {
    'summoner': '1.4',
    'game': '1.3'
}

REGIONS = {
    'europe_west': 'euw',
    'north_america': 'na'
}
