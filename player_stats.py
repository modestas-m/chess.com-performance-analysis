from chessdotcom import client, get_player_game_archives
import pprint
import requests
import pandas as pd

username = 'chiopra'

printer = pprint.PrettyPrinter()

def print_stats(username):
    data = client.get_player_stats(username, tts=0)
    printer.pprint(data.json)

def get_games(username):
    data = get_player_game_archives(username)
    for key,value in data.json.items():
        for url in value:
            games = requests.get(url).json()
            print(url)
            print()
            print()
            print()
            # printer.pprint(games['games'])
            for game in games['games']:
                print(game['time_class'])
                print(type(game))
                df = pd.DataFrame.from_dict(game, orient = 'columns')
                print(df)
                print
                print(df.columns)
                string = df['pgn'].to_string(index=False)
                print(string)
                for i in string.split('"'):
                    print(i)
                break;
            break;
              
    # for i in data['Archives']:
    #     print(i)
    # printer.pprint(data.json)

get_games(username)

# print(requests.get('https://www.chess.com/game/live/1221711014').content())