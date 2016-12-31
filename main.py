from RiotAPI import RiotAPI
import functools
import plotly as py
from plotly.graph_objs import Pie, Layout

def main():
    api = RiotAPI('RGAPI-be85ef47-a17a-49d7-a453-587388a74d74')
    reference = api.summoner_by_name('Shijou Kurumi')
    print(reference['shijoukurumi'])
    sub_reference = reference['shijoukurumi']
    summoner_name = sub_reference['name']
    summoner_id = sub_reference['id']
    print(summoner_name)
    print(summoner_id)

    game = api.summoner_game(summoner_id)
    games = game["games"]
    # print(ward_place)
    number_of_games = 0
    ward_count = 0
    list_of_game_stats = []
    for match in games:
        # print(d)
        if match['stats']['wardPlaced']:
            number_of_games += 1
            # print(d['stats']['wardPlaced'])
            ward_count += match['stats']['wardPlaced']
            game_stats = {
                'game_number': number_of_games,
                'game_sub_type': match['subType'],
                'ward_placed': match['stats']['wardPlaced'],
                'time_played': match['stats']['timePlayed']
            }
            list_of_game_stats.append(game_stats)
    print('Number of games taken into account is', number_of_games)
    print('Ward count is', ward_count, 'over', number_of_games, 'games.')
    average_ward_count = ward_count / number_of_games
    print('Average ward count is', average_ward_count)
    for k in list_of_game_stats:
        time_played = k['time_played']
        mins = int(time_played / 60)
        secs = int(((time_played / 60) - mins) * 60)
        wards_per_min = float("{0:.2f}".format(k['ward_placed'] / mins))
        print('Game number:', k['game_number'], 'Game sub type:',
            k['game_sub_type'], 'Wards placed:', k['ward_placed'],
            'Wards per min:', wards_per_min, 'Game time:', mins, 'mins', secs,
            'secs')

    """
    py.offline.plot({
        'data': [{
              'labels': [summoner_name, 'player 2'],
              'values': [average_ward_count, 50],
              'type': 'pie'}],

        'layout': {'title': 'Hello World!'}
    })
    """

if __name__ == "__main__":
    main()
