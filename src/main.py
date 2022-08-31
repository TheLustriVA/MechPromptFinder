import routing as rt
import dynamic_scrape as ds
from pathlib import Path 
from alive_progress import alive_bar
from json import JSONDecodeError
from selenium.common.exceptions import WebDriverException
from pathlib import Path
import json

PATH = ds.get_path()

if __name__ == "__main__":
    def update_list(json_list, path, website):
        """
        define a function that removes a url from the json_list file if the uuid in the url matches the stem of a json file in the path argument.
        Then update the json_list with new URLs from the website argument.
        """
        updates = 0
        for file in path.rglob('*.json'):
            if file.stem in json_list:
                json_list.remove(file.stem)
                updates += 1
        update_list = ds.update_target_list(PATH, website, json_list)
        old_length = len(json_list)
        for piece in update_list:
            json_list.append(piece)
        new_length = len(json_list)
        print(f"{updates} removed, leaving {old_length}. {new_length - old_length} added, leaving {new_length}.")
        return json_list
 
    def main(path):
        target_list = rt.get_url_list_from_file(Path.cwd() / "target_list.json")
        with alive_bar(len(target_list), length=30, dual_line=True, theme='smooth') as bar:
            for piece in target_list:
                if rt.ignore_loaded(piece):
                    bar()
                    continue
                try:
                    ds.scrape_piece(piece, PATH, ds.get_UUID())
                except JSONDecodeError:
                    continue
                except WebDriverException:
                    continue
                bar()
    
    def update_target_file(path, new_list:list):
        with open(path, 'r', encoding="utf-8") as f:
            target_list_info = json.load(f)
        target_list_info['creation_archive_list'] = new_list
        with open(path, "w", encoding="utf-8") as f:
            json.dump(target_list_info, f, indent=4)
        


update_target_file(Path.cwd() / "target_list.json", update_list(rt.get_url_list_from_file(Path.cwd() / "target_list.json"), Path.cwd() / "data" / "feverdream_scrape", "https://www.feverdreams.app/recent/1"))

main(PATH)

#     def count_records(file):        
#         with open(file, 'r', encoding='utf-8') as f:
#             scrape_list = json.load(f)
#             print(f"So far we have scraped {len(scrape_list)} pieces.")
# 
#     def first_batch_combine():
#         results = rt.combine_data_files(Path.cwd() / "data", ["public_metadata", "img_src", "prompt"])
#         print(f"The new file is called {results[0]}.")
#         if results[1]:
#             for fail in results[1]:
#                 print(f"{fail} failed to load.")
# 
# 
# print(rt.process_all_data_files(rt.is_json, (rt.process_all_data_files(rt.lacks_private_metadata, rt.add_mlva_uuid, dry_run=True)), dry_run=True))

        
