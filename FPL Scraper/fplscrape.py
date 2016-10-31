import requests
import json

player_id = []
all_data = {}
errors = {}

def parse_data(data):
    json_parsed = json.loads(data)
    print(json_parsed)

def get_current_stats():
    current_url = "https://fantasy.premierleague.com/drf/bootstrap-static"
    r = requests.get(current_url)


def get_old_stats(url_range):
    for i in range(url_range):
        player_url = "https://fantasy.premierleague.com/drf/element-summary/{}".format(i)
        print(i)
        r = requests.get(player_url)

        # Skip empty pages
        if r.status_code != 200:
            errors[i] = r.status_code
            print("Not found.\n")
            continue

        # Put player name as dictionary key. Remaining data is the key for each entry
        temp = r.json()
        print(temp)

get_old_stats(5)