from time import sleep
from requests_html import HTMLSession
import json
from pprint import pprint
from alive_progress import alive_bar
 


sesh = HTMLSession()
get = {
        "GET": {
		"scheme": "https",
		"host": "api.feverdreams.app",
		"filename": "/job/cc5abd14-7ddf-4d0d-bc59-c02d161b8d03",
		"remote": {
			"Address": "104.26.0.188:443"
		    }
        }
    }
headers = {
    "Host" : "api.feverdreams.app",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept" : "*/*",
    "Accept-Language" : "en-US,en;q=0.5",
    "Accept-Encoding" : "gzip, deflate, br",
    "Referer" : "https://www.feverdreams.app/",
    "Origin" : "https://www.feverdreams.app",
    "DNT" : "1",
    "Connection" : "keep-alive",
    "Sec-Fetch-Dest" : "empty",
    "Sec-Fetch-Mode" : "cors",
    "Sec-Fetch-Site" : "same-site"
}

def site_request(url, headers):
    session = sesh.get(url,headers=headers)
    return session

def site_request_html(session):
    session.html.render(sleep=1, keep_page=True, scrolldown=1)
    return session.html.html

# with open("test.html", "w", encoding="utf-8") as f:
#     f.write(site_request(url))

payload_list = []

# with open("main_payload.json", "w+", encoding="utf-8") as f:
#     json.dump({"payload_docs" : [] }, f, indent=2)

with alive_bar(300) as bar:
    for idx in range(1, 300):
        url = f"https://api.feverdreams.app/v2/recent/all/50/{idx}"
        get_back = site_request_html(site_request(url, headers))
        payload = json.loads(get_back[25:-14])
        
        with open("main_payload.json", "r", encoding="utf-8") as f:
            data_body = json.load(f)
        with open("main_payload.json", "w", encoding="utf-8") as g:
            data_body['payload_docs'].extend(payload)
            json.dump(data_body, g, indent=2)
        bar()