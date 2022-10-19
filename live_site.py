from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://news.ycombinator.com/")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title)

heading_tags = soup.select(selector=".titleline > a")
# pprint(heading_tags)
# pprint(len(heading_tags))

score_tags = soup.select(selector=".score")
# pprint(score_tags)
scores = [int(tag.getText().split(" ")[0]) for tag in score_tags]
# print(scores)

articles = [(tag.getText(), tag.get("href"))
            for tag in heading_tags]
# pprint(articles)

# * find the index of the largest score
targed_idx = scores.index(max(scores))
# print(targed_idx)

top_article = articles[targed_idx]

print(top_article)

# ! always check a website's /robots.txt to see the rules about scrapping their data
