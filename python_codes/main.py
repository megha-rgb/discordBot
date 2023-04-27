import os
import json
import bot
def get_json_path():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\user_data\userData.json"

def main():
    file_name = get_json_path()
    f = open(file_name)
    dict_data = json.load(f)

    bot.VeggieBot(dict_data)

if __name__ == "__main__":
    main()