from RiotAPI import RiotAPI
import functools

def main():
    api = RiotAPI('RGAPI-be85ef47-a17a-49d7-a453-587388a74d74')
    reference = api.summoner_by_name('Shijou Kurumi')
    print (reference['shijoukurumi'])
    sub_reference = reference['shijoukurumi']
    summoner_name = sub_reference['name']
    summoner_id = sub_reference['id']
    print(summoner_name)
    print(summoner_id)

    game = api.summoner_game(summoner_id)
    ward_place = game["games"]
    #print(ward_place)
    number_of_games = 0
    ward_count = 0
    for d in ward_place:
        #print(d)
        if d['stats']:
            #print(d['stats'])
            if d['stats']['wardPlaced']:
                number_of_games += 1
                #print(d['stats']['wardPlaced'])
                ward_count += d['stats']['wardPlaced']
    print('Number of games taken into account is', number_of_games)
    print('Ward count is', ward_count, 'over', number_of_games, 'games.')
    average_ward_count = ward_count / number_of_games
    print('Average ward count is', average_ward_count)

    #print(functools.reduce(lambda r, d: r.update(d) or r, ward_place, {}))

if __name__ == "__main__":
    main()
