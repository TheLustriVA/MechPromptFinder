from time import sleep
from requests_html import HTMLSession
import json
from pprint import pprint
import pandas
 

url = "https://api.feverdreams.app/job/cc5abd14-7ddf-4d0d-bc59-c02d161b8d03"
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
    "Host": "api.feverdreams.app",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.feverdreams.app/",
    "Origin": "https://www.feverdreams.app",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site"
}


def site_request(url, headers):
    session = sesh.get(url,headers=headers)
    return session

def site_request_html(session):
    session.html.render(sleep=1, keep_page=True, scrolldown=1)
    return session.html.html

# with open("test.html", "w", encoding="utf-8") as f:
#     f.write(site_request(url))

payload = json.loads(site_request_html(site_request(url, headers))[25:-14])
payload['discoart_tags'].get('_status').pop('loss', None)
discoart_tags = payload['discoart_tags'].copy()
payload.pop('discoart_tags', None)
# print("*******\nPayload:")
# pprint(payload)
# print("*******\nDiscoart_tags:")
# pprint(discoart_tags)

record_id = payload['_id'].get('$oid')

payload_keys = list(payload.keys())
discoart_tags_keys = list(discoart_tags.keys())

print(f"Payload_keys len: {len(payload_keys)}\n Discoart_tags_keys len: {len(discoart_tags_keys)}")

# define a function called "differences" that returns a list of the differences between two lists.
common_list = set(payload_keys+discoart_tags_keys)

print(common_list)

