import requests, sys, csv

PLAYER_NAMES = []
PLAYER_DATA_DICT = {}


# Used to convert the dictionaries of JSON into a CSV files
# def dict_to_csv(player_data_dict):
#     player_data_dict = 1    # history-past, history, fixtures
#     return player_data_dict


# Use FPL API bootstrap endpoint to get player names for the keys of PLAYER_DATA_DICT.
# Also used to define number of players in catalogued in FPL (to avoid requests in other functions)
def get_player_names():
    r = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')
    print('Getting Player Names...')

    bootstrap_data = r.json()
    print(bootstrap_data)
    global NUM_PLAYERS
    NUM_PLAYERS = len(bootstrap_data['elements'])

    for i in range(NUM_PLAYERS):
        PLAYER_NAMES.append(bootstrap_data['elements'][i]['first_name']
                            + ' '
                            + bootstrap_data['elements'][i]['second_name'])

    print(PLAYER_NAMES)


# Grab a player's current season's statistics from the API static bootstrap JSON
# Cycle through FPL API endpoint (also in JSON) for individual players' past season's stats
# Combine all the data to create a singular dictionary file
def get_player_json():
    misses = 0
    player_url = 'https://fantasy.premierleague.com/drf/element-summary/{}'

    for i in range(590, NUM_PLAYERS+1):
        r = requests.get(player_url.format(i))
        print('Grabbing Player #' + str(i))

        # Skip broken URLs
        if r.status_code != 200:
            misses += 1
            print('BROKEN URL @ PLAYER #: ' + str(i) + '\n')
            # More than one miss in a row - end of requests!
            if misses > 1:
                print('Two broken URls in a row... Something is wrong with your connection or the API.\n')
                sys.exit()
            continue

        # Reset 'missing' counter.
        misses = 0

        player_id = i
        # match_id = player_json['history'][0]['fixture']


        player_json = r.json()
        parsed_player_data = {'Past Seasons Stats': player_json['history_past'],
                              'Games This Season': player_json['history'],
                              'Future Fixtures': player_json['fixtures']}

        PLAYER_DATA_DICT[PLAYER_NAMES[i-1]] = parsed_player_data
        i += 1


get_player_names()
print()
get_player_json()

for player in PLAYER_DATA_DICT:
    if len(PLAYER_DATA_DICT[player]['Past Seasons Stats']) == 0:
        print(player)
        print('Games This Season : ', PLAYER_DATA_DICT[player]['Games This Season'])
        print('Future Fixtures : ',PLAYER_DATA_DICT[player]['Future Fixtures'])
        print()
    else:
        print(player)
        for json in PLAYER_DATA_DICT[player]:
            print(json, ':', PLAYER_DATA_DICT[player][json])
        print()
