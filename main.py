from RiotAPI import RiotAPI
import functools


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
    ward_place = game["games"]
    # print(ward_place)
    number_of_games = 0
    ward_count = 0
    list_of_game_stats = []
    for d in ward_place:
        # print(d)
        if d['stats']['wardPlaced']:
            number_of_games += 1
            # print(d['stats']['wardPlaced'])
            ward_count += d['stats']['wardPlaced']
            game_stats = {
                'game_number': number_of_games,
                'ward_in_game': d['stats']['wardPlaced']
            }
            list_of_game_stats.append(game_stats)
    print('Number of games taken into account is', number_of_games)
    print('Ward count is', ward_count, 'over', number_of_games, 'games.')
    average_ward_count = ward_count / number_of_games
    print('Average ward count is', average_ward_count)
    for k in list_of_game_stats:
        print('Game number:', k['game_number'], 'Wards placed:',
              k['ward_in_game'])

if __name__ == "__main__":
    main()
