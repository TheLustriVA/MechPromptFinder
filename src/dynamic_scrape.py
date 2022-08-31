# Run this code first to set up the scraper.

import uuid
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import json
from pathlib import Path

PATH = "F:\\" 
START = "https://www.feverdreams.app/recent/1"
TARGET_LIST = []
DATA_DICT = { "creations" : [] }


def get_path():
    return "F:\\"

# write a function that takes in a list of elements and returns a list of hrefs
def href_list(elements):
    href_list = []
    for element in elements:
        href_list.append(element.get_attribute("href"))
    return href_list


def create_target_archive(driver_path, current_page:str)->list:
    """
    Define a function called create_target_archive that takes a driver, a current page, a next page and a target list. The function should:
    1. It should create a webdriver called 'driver' and point it at the current page.
    2. Find and create a list called 'browse_list' of urls in the href attributes of all 'a' elements that are children of 'div' elements.
    3. It should create a dictionary called 'results_dict' with the keys 'next_page' with the value browse_list[1] and 'new_targets' with browse_list[2:-7].
    4. It should call driver.quit() and sleep for 5 seconds.
    5. It should return results_dict.
    """
    driver = webdriver.Chrome(driver_path + "chromedriver.exe")
    driver.get(current_page)
    time.sleep(15)
    browse_list = href_list(driver.find_elements(By.XPATH, "//div/a[@href]"))
    results_dict = { "next_page" : browse_list[1], "new_targets" : browse_list[2:-7] }
    time.sleep(5)
    driver.quit()
    return results_dict  

def populate_target_archive(archive_dict:dict)->list:
    """Loop through the target archive and add the new targets to the target list.

    Args:
        archive_dict (dict): _The return value of create_target_archive._

    Returns:
        list: _A list of pages to scrape._
    """
    cargo_dict = create_target_archive(PATH, START)

    for idx in range(1, 310):
        cargo_dict = create_target_archive(PATH, cargo_dict["next_page"])
        TARGET_LIST.extend(cargo_dict["new_targets"])
        with open("target_list.txt", "a", encoding="utf-8") as f:
            for target in cargo_dict['new_targets']:
                f.write(target + "\n")
    return TARGET_LIST

def update_target_list(driver_path, current_page:str, url_list:list)->list:
    """
    Define a function that takes in a diver, a current page, and a list of URLs. The function should:
    1. It should create a webdriver called 'driver' and point it at the current page.
    2. It should create a list of hrefs called 'new_urls' using the href_list function on driver.find_elements(By.XPATH, "//div/a[@href]")
    3. The function should then call itself recursively until elements in the 'new_urls' list return true for the is_done function.
    4. It should return the list of URLs.
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(driver_path + "chromedriver.exe", options=options)
    driver.get(current_page)
    time.sleep(10)
    new_urls = href_list(driver.find_elements(By.XPATH, "//div/a[@href]"))
    for url in new_urls:
        if url not in url_list:
            url_list.append(url)
            driver.quit()
            time.sleep(1)
            update_target_list(driver_path, url, url_list)
    return url_list
    

def url_to_json(url:str, driver:webdriver)->str:
    """
    define a function called 'url_to_json' that takes in a url and a driver. The function should:
    1. It should take the driver and point it at the url.
    2. it should load the page and wait for the page to load.
    3. It should load the entire contents of the page into a json string.
    """
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    return page_source

def get_UUID():
    return str(uuid.uuid4())

mlva_uuid = get_UUID()

def get_public_metadata(source_json, identifier):
    key_list = [
        "transformation_percent",
        "clip_models_schedules",
        "diffusion_model_config",
        "width_height",
        "clip_guidance_scale",
        "skip_event",
        "sat_scale",
        "batch_name",
        "name_docarray",
        "cut_innercut",
        "skip_augs",
        "clip_denoised",
        "seed",
        "use_vertical_symmetry",
        "init_scale",
        "steps",
        "use_secondary_model",
        "text_prompts",
        "gif_fps",
        "cut_icgray_p",
        "truncate_overlength_prompt",
        "clip_models",
        "cut_overview",
        "display_rate",
        "use_horizontal_symmetry",
        "eta",
        "perlin_init",
        "init_image",
        "clamp_max",
        "randomize_class",
        "on_misspelled_token",
        "gif_size_ratio",
        "save_rate",
        "rand_mag",
        "range_scale",
        "tv_scale",
        "n_batches",
        "cut_ic_pow",
        "clamp_grad",
        "batch_size",
        "stop_event",
        "text_clip_on_cpu",
        "diffusion_sampling_mode",
        "diffusion_model",
        "cutn_batches",
        "cut_schedules_group",
        "skip_steps",
        "perlin_mode"
    ]

    
    public_metadata = {
        "mlva_uuid" : identifier,
        "piece_metadata": []
    }

    with open(source_json, "r", encoding='utf-8') as f:
        metadata = json.load(f)
        
    for key in metadata['discoart_tags']:
        if key in key_list:
            try:
                public_metadata['piece_metadata'].append(f"{key}={metadata[key]}")
            except KeyError:
                public_metadata['piece_metadata'].append(f"{key}=Null")
        else:
            pass

    return public_metadata

def get_private_metadata(source_json, identifier):
    
    private_metadata = {
        "mlva_uuid" : identifier,
        "piece_metadata": []
    }

    with open(source_json, "r", encoding='utf-8') as f:
        metadata = json.load(f)
        
    for key in metadata:
        try:
            private_metadata['piece_metadata'].append(f"{key}={metadata[key]}")
        except KeyError:
            private_metadata['piece_metadata'].append(f"{key}=Null")

    return private_metadata


def url_to_json(url:str, driver:webdriver)->str:
    """
    define a function called 'url_to_json' that takes in a url and a driver. The function should:
    1. It should take the driver and point it at the url.
    2. it should load the page and wait for the page to load.
    3. It should load the entire contents of the page into a json string.
    """
    driver.get(url)
    time.sleep(5)
    page_source = driver.find_element(By.TAG_NAME, "body").get_attribute("innerHTML")
    time.sleep(10)
    with open("F:\dogma\CentralDogma\MechArtResearch\MechPromptFinder\src\metadata_cache.json", "w+", encoding='utf-8') as f:
        print(page_source, file=f)
    return "F:\dogma\CentralDogma\MechArtResearch\MechPromptFinder\src\metadata_cache.json"

def url_to_metadata_url(url:str)->str:
    """
    define a function called 'url_to_metadata_url' that takes in a url and returns a url to the metadata.
    """
    return url.replace("/piece/", "/job/").replace("www", "api")

def scrape_piece(url:str, driver_path:str, mlva_uuid:uuid.uuid4)->str:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(driver_path + "chromedriver.exe", options=options)
    driver.get(url)
    time.sleep(3)
    try:
        identifier = driver.find_elements(By.XPATH, "//div/h4")[0].text,
    except IndexError as IDE:
        return IDE
    img_src = driver.find_elements(By.XPATH, "//a/img")[0].get_attribute("src"),
    try:
        image_path = f"F:\dogma\CentralDogma\MechArtResearch\MechPromptFinder\src\data\images\{identifier[0]}.png"
    except WebDriverException as wde:
        return wde
    driver.find_elements(By.XPATH, "//a/img")[0].screenshot(image_path)
    prompt = driver.find_elements(By.XPATH, "//div/code")[0].text,
    public_metadata = get_public_metadata(url_to_json(url_to_metadata_url(url), driver), mlva_uuid),
    private_metadata = get_private_metadata(url_to_json(url_to_metadata_url(url), driver), mlva_uuid),
    piece_cache = {
        "identifier":identifier,
        "img_src": img_src,
        "prompt": prompt,
        "public_metadata": public_metadata,
        "private_metadata": private_metadata,
    }

    time.sleep(5)
    driver.quit()
    output_file = f"data/feverdream_scrape/{identifier[0]}.json"
    with open(output_file, "w", encoding='utf-8') as f:
        json.dump(piece_cache, f, indent=4)
    return output_file