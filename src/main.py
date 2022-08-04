import routing as rt
import dynamic_scrape as ds
from pathlib import Path 
from alive_progress import alive_bar
from json import JSONDecodeError
from selenium.common.exceptions import WebDriverException

PATH = ds.get_path()

if __name__ == "__main__":
    target_list = rt.get_url_list_from_file(Path.cwd() / "data" / "target_list.json")
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