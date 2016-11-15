from RiotAPI import RiotAPI

def main():
    api = RiotAPI('RGAPI-be85ef47-a17a-49d7-a453-587388a74d74')
    reference = api.get_summoner_by_name('Shijou Kurumi')
    print (reference['shijoukurumi'])
    sub_reference = reference['shijoukurumi']
    summoner_name = sub_reference['name']
    summoner_id = sub_reference['id']
    print(summoner_name)
    print(summoner_id)

    test_summoner_id = api.get_summoner_id(summoner_id)
    print(test_summoner_id)

if __name__ == "__main__":
    main()
