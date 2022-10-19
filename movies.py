from bs4 import BeautifulSoup
from pprint import pprint
import requests

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movie_title_tags = soup.find_all(name="h3", class_="jsx-4245974604")
pprint(movie_title_tags)
titles = [tag.getText() for tag in movie_title_tags]

ordered_movies = titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in ordered_movies:
        file.write(f"{movie}\n")
