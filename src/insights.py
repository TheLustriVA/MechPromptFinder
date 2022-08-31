import json
from pprint import pprint

with open("main_payload.json", "r", encoding="utf-8") as f:
    payload = json.load(f)

main_payload = payload['payload_docs'][0]

payload_keys = list(main_payload.keys())

# define a function that creates a list of new seperate dictionary for the keys in the following list:
table_list = [
    "_id",
    "width_height",
    "clip_models",
    "timestamp",
    "last_preview",
    "transformation_percent",
    "dominant_color",
    "palette",
    "thumbnails",
    "discoart_tags",
    "time_completed",
    "dt_timestamp",
    "userdets"
]

def new_dicts(payload_keys, table_list):
    new_dicts = []
    for key in table_list:
        new_dicts.append({key: main_payload[key]})
    return new_dicts

for new_dict in new_dicts(payload_keys, table_list):
    pprint(new_dict)
    input("Press Enter to continue...")

    

