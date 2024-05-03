import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

titles = [i.getText() for i in soup.find_all(name="h3", class_="title")]
movie_titles = titles[::-1]
# titles.reverse()

with open("./movies.txt", "w") as file:
    for i in movie_titles:
        file.write(f"{i}\n")
      