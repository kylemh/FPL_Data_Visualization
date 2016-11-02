import requests

PLAYER_NAMES = []
PLAYER_DATA_DICT = {}


# Used to choose the relevant data
def munge_data(dict):
    return


# Use FPL API bootstrap endpoint to get player names.
def get_player_names():
    r = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')
    print('Getting Player Names...')

    player = r.json()

    # TODO: Create dynamic manner of counting players listed in API
    for i in range(598):
        PLAYER_NAMES.append(player['elements'][i]['first_name'] + ' ' + player['elements'][i]['second_name'])

    print(PLAYER_NAMES)


# Cycle through FPL API endpoint for individual players' past history.
def get_player_past():
    misses = 0
    player_id = 595

    while True:
        player_url = 'https://fantasy.premierleague.com/drf/element-summary/{}'.format(player_id)
        print('Grabbing Player #' + str(player_id))
        r = requests.get(player_url)

        # Skip broken URLs
        if r.status_code != 200:
            misses += 1
            print('BROKEN URL @ PLAYER #: ' + str(player_id) + '\n')
            player_id += 1
            # More than one miss in a row - end of requests!
            if misses > 1:
                print('Two broken URls in a row... Were (likely) through all the players!')
                break
            continue

        # Reset 'missing' counter.
        misses = 0

        try:
            PLAYER_DATA_DICT[PLAYER_NAMES[player_id-1]] = r.json()
        except ValueError:
            print('FAILED TO PARSE PLAYER #' + str(player_id) + '\n')

        player_id += 1


get_player_names()
print()
get_player_past()
print(PLAYER_DATA_DICT)
