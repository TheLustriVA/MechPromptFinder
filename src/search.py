import json
from pathlib import Path
from json import JSONDecodeError
from pprint import pprint

def SearchWord(word, path, filter="results"):
    return_dict = {
        "results": [],
        "JSONError" : [],
        "AttributeError" : [],
        "KeyError" : []
    }
    filepath = Path(path)
    for file in filepath.rglob('*.json'):
        with open(file, "r", encoding='utf-8') as f:
            try:
                data = json.load(f)
            except JSONDecodeError as JDE:
                return_dict['JSONError'].append((f"{file} has no text_prompts - JSONERROR: {JDE}"))
                continue
            try:
                prompt = data['text_prompts'].get('0')
            except AttributeError as AE:
                return_dict['AttributeError'].append((f"{file} has no text_prompts - ATTRIBUTEERRROR: {AE}"))
                continue
            except KeyError as KE:
                prompt = data['prompt']
            #print(prompt)
            for line in prompt:
                if word in line:
                    return_dict['results'].append([file, prompt])
    return return_dict[filter]

pprint(SearchWord("anime", "data/", "JSONError"))

