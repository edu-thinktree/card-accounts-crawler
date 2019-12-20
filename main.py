import sys
import requests
from bs4 import BeautifulSoup as bs

indeed_result = requests.get(
    "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%EC%98%81%EC%96%B4&l=%EC%9D%B4%EC%B2%9C")

indeed_soup = bs(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')

spans = []
for page in pages:
    spans.append(page.find_all('span'))
print(spans[0:-1])
