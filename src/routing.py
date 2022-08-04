# import pandas as pd
import json
from pathlib import Path


def dir_tree(directory):
    print(f"+ {directory}")
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '   ' * depth
        print(f"{spacer}{'+'*depth} {path.name}")

def rename_files():
    """
    define a function that iterates through every file in the directory tree below the CWD and renames them to the the directory name and a unique number:
    each file should have the format <directory_parent>/<directory_name><unique_number>.<file_extension>
    """
    for idx, path in enumerate(Path.cwd().rglob('*')):
        if path.is_file():
            path.rename(path.parent / f"{path.parent.name}{idx}{path.suffix}")
        else:
            pass
    dir_tree(Path.cwd())
    return None


def is_json(file_path):
    """
    Define a function that reads the entire contents of a .txt file and returns true if it is a valid .json file. Return False otherwise.
    """
    if file_path.suffix == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                json.load(f)
                return True
            except json.JSONDecodeError:
                return False

def rename_as_json(path):
    """
    Define a function that changes the file extension of a file to .json.
    """
    path.rename(path.parent / f"{path.stem}.json")
    return None


def parse_all_data_files(function)->list:
    """
    Define a function that takes a function as an argument and iterates through every file in the directory tree below the CWD and applies the function to each file.
    """
    data = []
    for path in Path.cwd().rglob('*'):
        if path.is_file():
            data.append(function(path))
        else:
            pass
    return data

def process_all_data_files(check_function, action_function, dry_run:bool) -> list:
    """
    Define a function that iterates through every file in the directory tree below the CWD and applies the check_function to each file.
    If the check_function returns True, the action_function is applied to the file.
    
    If dry_run is True, the action_function is not applied to the file. A list of files that would have been processed is returned.
    """
    wet_run_files = []
    dry_run_files = []
    for path in Path.cwd().rglob('*'):
        if path.is_file():
            if check_function(path):
                if dry_run:
                    dry_run_files.append(path)
                else:
                    action_function(path)
                    wet_run_files.append(path)
            else:
                pass
        else:
            pass
    if dry_run:
        return dry_run_files
    else:  
        return wet_run_files



def combine_data_files(directory):
    """
    Define a function that combines all .json files in the directory tree below the CWD into a single .json file.
    """
    data = []
    failures = []
    for path in directory.rglob('*.json'):
        with open(path, 'r', encoding='utf-8') as f:
            try:
                data.append(json.load(f))
            except json.decoder.JSONDecodeError as j_error:
                try:
                    kicked_path = correct_json_properties(path)
                    with open(kicked_path, 'r', encoding='utf-8') as f:
                        data.append(json.load(f))
                except json.decoder.JSONDecodeError as second_j_error:
                    failures.append(path)
                    continue
    with open(directory / 'combined.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return (f.__str__(), failures)

def correct_json_properties(path):
    """
    Define a function that encloses all json properties in quotes.
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return path

def convert_archive_list_to_json(txt_file_path, output_file):
    """
    Define a function that converts the archive list .txt file into a .json file.
    """
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()
    json_structure = {
        "archive_list_version": "0.1.0",
        "archive_creation_date": "2022-08-01",
        "archive_site_sources": [
            "https://feverdreams.app"
        ],
        "creation_archive_list": [
            
        ]
    }
    for item in data:
        json_structure['creation_archive_list'].append(item.strip("\n"))
    with open(output_file, 'w+', encoding='utf-8') as f:
        json.dump(json_structure, f, indent=4)
    return output_file

def get_url_list_from_file(file_path, filetype='json', dict_key='creation_archive_list'):
    """
    Define a function that reads the contents of a file and returns a list of all URLs in the file.
    
    Assumes that json files have a list of URLs under a single key.
    
    Assumes that text files are line-delimited lists of URLs.
    
    TO-DO: Add support for other filetypes like csv, excel, yaml, etc.
    """
    if filetype == 'json':
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data[dict_key]
    elif filetype == 'txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        return [item.strip("\n") for item in data]
    
def ignore_loaded(identifier:str)->bool:
    """
    Define a function that takes an identifier and returns True if it matches the stem of any file in the 'data' directory below the CWD.
    """
    for path in Path.cwd().joinpath('data').rglob('*'):
        if path.stem == identifier:
            return True
        else:
            pass
    return False