from time import sleep
from requests_html import HTMLSession

url = "https://www.feverdreams.app/recent/1"
sesh = HTMLSession()

def site_request(url):
    response = sesh.get(url)
    print(response)
    response.html.render(sleep=1, keep_page=True, scrolldown=1)
    return response.html.html

with open("test.html", "w", encoding="utf-8") as f:
    f.write(site_request(url))