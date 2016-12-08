import requests
import sys
import csv

PLAYER_NAMES = []
PAST_SEASON_STATS = {}
CURR_SEASON_STATS = {}


# Use FPL API bootstrap endpoint to get player names and current season stats.
# Also used to define number of players in catalogued in FPL (to avoid unnecessary HTTP requests)
def get_player_names():
    r = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')
    print('\n...Getting player names and current season stats...')

    bootstrap_data = r.json()
    global NUM_PLAYERS
    NUM_PLAYERS = len(bootstrap_data['elements'])

    for i in range(NUM_PLAYERS):
        PLAYER_NAMES.append(bootstrap_data['elements'][i]['first_name']
                            + ' '
                            + bootstrap_data['elements'][i]['second_name'])
        curr_season_data = {'Season 2016/2017':   bootstrap_data['elements'][i]['id']
                                                + bootstrap_data['elements'][i]['minutes']
                                                + bootstrap_data['elements'][i]['goals_scored']
                                                + bootstrap_data['elements'][i]['assists']
                                                + bootstrap_data['elements'][i]['clean_sheets']
                                                + bootstrap_data['elements'][i]['goals_conceded']
                                                + bootstrap_data['elements'][i]['own_goals']
                                                + bootstrap_data['elements'][i]['penalties_saved']
                                                + bootstrap_data['elements'][i]['penalties_missed']
                                                + bootstrap_data['elements'][i]['yellow_cards']
                                                + bootstrap_data['elements'][i]['red_cards']
                                                + bootstrap_data['elements'][i]['saves']
                                                + bootstrap_data['elements'][i]['ea_index']
                                                + bootstrap_data['elements'][i][int('ict_index')]
                                                + bootstrap_data['elements'][i][float('selected_by_percent')]}
        CURR_SEASON_STATS[PLAYER_NAMES[i - 1]] = curr_season_data

    print(PLAYER_NAMES)


# Grab a player's current season's statistics from the API static bootstrap JSON
# Cycle through FPL API endpoint (also in JSON) for individual players' past season's stats
# Combine all the data to create a singular dictionary file
def get_player_json():
    misses = 0
    player_url = 'https://fantasy.premierleague.com/drf/element-summary/{}'

    # Convert range from i to NUM_PLAYERS+1 when running complete
    for i in range(590, NUM_PLAYERS + 1):
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

        player_json = r.json()
        parsed_player_data = {'Past Seasons Stats': player_json['history_past']}

        PAST_SEASON_STATS[PLAYER_NAMES[i - 1]] = parsed_player_data
        i += 1


# ############ #
# Main Program #
################
get_player_names()
print()
get_player_json()

for player in PAST_SEASON_STATS:
    if len(PAST_SEASON_STATS[player]['Past Seasons Stats']) == 0:
        print(player)
        print('Games This Season : ', PAST_SEASON_STATS[player]['Games This Season'])
        print('Future Fixtures : ', PAST_SEASON_STATS[player]['Future Fixtures'])
        print()
    else:
        print(player)
        for json in PAST_SEASON_STATS[player]:
            print(json, ':', PAST_SEASON_STATS[player][json])
        print()
