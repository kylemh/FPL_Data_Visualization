import requests, json, shutil, hashlib, glob, os

PLAYER_NAMES = []
PLAYER_DATA_DICT = {}


# Used to choose the relevant data
def munge_data(dict):
    return


# Use FPL API bootstrap endpoint to get player names for the keys of PLAYER_DATA_DICT.
def get_player_names():
    r = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')
    print('Getting Player Names...')

    player = r.json()

    # TODO: Create dynamic manner of counting players listed in API
    for i in range(598):
        PLAYER_NAMES.append(player['elements'][i]['first_name'] + ' ' + player['elements'][i]['second_name'])

    print(PLAYER_NAMES)


# Cycle through FPL API endpoint for individual players' stats and create a singular JSON file.
def get_player_json():
    misses = 0
    player_id = 597
    player_url = 'https://fantasy.premierleague.com/drf/element-summary/{}'

    while True:
        print('Grabbing Player #' + str(player_id))
        r = requests.get(player_url.format(player_id))

        # Skip broken URLs
        if r.status_code != 200:
            misses += 1
            print('BROKEN URL @ PLAYER #: ' + str(player_id) + '\n')
            player_id += 1
            # More than one miss in a row - end of requests!
            if misses > 2:
                print('Three broken URls in a row... Were (likely) through all the players!\n')
                break
            continue

        # Reset 'missing' counter.
        misses = 0

        try:
            PLAYER_DATA_DICT[PLAYER_NAMES[player_id-1]] = r.json()
        except ValueError:
            print('FAILED TO PARSE PLAYER #' + str(player_id) + '\n')

        player_id += 1

    fn = "data/players.{}.json"
    with file(fn, 'w') as outfile:
        json.dump(PLAYER_DATA_DICT, outfile, indent = 2)

get_player_names()
print()
get_player_json()
print(PLAYER_DATA_DICT)
