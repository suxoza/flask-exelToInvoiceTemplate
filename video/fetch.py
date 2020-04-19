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



# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# executable_path = "/usr/local/bin/chromedriver"
# os.environ["webdriver.chrome.driver"] = executable_path

# chrome_options = Options()
# chrome_options.add_extension(executable_path)

# driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
# driver.get("https://tubitv.com/movies/490975/minutes_to_midnight?tracked=1")
#driver.quit()

# browser.get(url)
# print(browser)



# import mechanize
# br = mechanize.Browser()
# resp = br.open(url)
# print(resp.info())
# print(resp.read())

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re, sys, os
from selenium import webdriver
import time
url = 'https://tubitv.com/movies/490975/minutes_to_midnight?tracked=1'
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source



soup = BeautifulSoup(html, 'html.parser')

#blob:https://tubitv.com/1ace0e8a-aa17-4a63-a3d8-d3d3ee945a54

dv = soup.find('div', attrs={'id': 'hls'})
print(dv.video.get('src'))




# from pynav import Browser
# b = Browser()
# b.allow_all_content_types()
# b.go(url)
# b.verbose = True
# #print(b.r.links)

# # #print(b.r.links)
# for i in b.r.links:
# 	print(i)

