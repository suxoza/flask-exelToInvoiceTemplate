# await fetch("https://fastly.tubi.video/72f7c2e2-fae8-4944-ba38-2fbf0e5d3d5c/m7a3hgpy0t.m3u8?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiI3MmFkZGEyNy03YjliLTRlZDEtOWNkMS1lMzg1YzQyNTRjMDMiLCJleHAiOjE1NzQwMzA5MjIsInBsYXRmb3JtIjoid2ViIiwidXNlcl9pZCI6MH0.yqjqfP08vWLgdFOshQ3_whiSbnhm46REUZljIKTUtU8", {
#     "credentials": "omit",
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
#         "Accept": "*/*",
#         "Accept-Language": "en-US,en;q=0.5"
#     },
#     "referrer": "https://tubitv.com/movies/490975/minutes_to_midnight?tracked=1",
#     "method": "GET",
#     "mode": "cors"
# });



import sys, os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup

driver = webdriver.Firefox(executable_path = './geckodriver25')
# from selenium.webdriver.chrome.service import Service
# service = Service('/usr/local/bin/geckodriver25')
# service = Service('/usr/local/bin/geckodriver25')
# service.start()

#driver = webdriver.Remote(service.service_url)
sys.exit()
driver.get("https://tubitv.com/movies/490975/minutes_to_midnight?tracked=1")

html = driver.page_source

soup = BeautifulSoup(html, 'html5lib')

#blob:https://tubitv.com/1ace0e8a-aa17-4a63-a3d8-d3d3ee945a54

dv = soup.find('div', attrs={'id': 'hls'})
print(dv.video.get('src'))

# browser.get(url)
# print(browser)



# import mechanize
# br = mechanize.Browser()
# resp = br.open(url)
# print(resp.info())
# print(resp.read())



sys.exit()


req = Request(url, headers=hdr)
rd = response.read()
soup = BeautifulSoup(rd, 'html.parser')








from pynav import Browser
b = Browser()
b.allow_all_content_types()
b.go(url)
b.verbose = True
#print(b.r.links)

# #print(b.r.links)
for i in b.r.links:
	print(i)

