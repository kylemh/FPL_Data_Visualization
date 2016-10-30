import requests


all_data = {}
api_error = {}

def set_filepath(file_from_cloud):
    if platform.system() == "Mac"


for i in range(594):
    player_url = "https://fantasy.premierleague.com/drf/element-summary/{}".format(i)
    print("Scraping Player #: " + i + ".\n")
    r=requests.get(player_url)

    # Skip empty pages
    if r.status_code != 200:
        api_error[i] = r.status_code
        print("Not found.\n")
        continue

    # Put player name as dictionary key. Remaining data is the key for each entry
    temp = r.json()
    player_name = temp['web_name']
    print(player_name + "\n")
    all_data[player_name] = temp
