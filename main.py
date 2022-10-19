from bs4 import BeautifulSoup
from pprint import pprint
# import lxml

with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# * returns the first h1 tag it encounters
# print(soup.h1.string)
# print(soup.h1.getText())

# * find all tags query
link_tags = soup.find_all(name="a")

links = []
for link in link_tags:
    # * get the value of a specific attribute of the tag
    links.append(link.get("href"))

# pprint(links)

# * find a specific tag query (using id, class, etc...)
section_heading_tag = soup.find(name="h3", class_="heading")
# print(section_heading_tag.getText())

# * find a specific tag using css selectors syntax
company_link_tag = soup.select_one(selector="p a")
print(company_link_tag)
name_tag = soup.select_one(selector="#name")
print(name_tag)
section_heading_tags = soup.select(selector=".heading")
pprint(section_heading_tags)
