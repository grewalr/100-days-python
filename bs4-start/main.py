from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.prettify())

article_table_row = soup.find(id="40247604")
article_tag = article_table_row.find(name="span", class_="titleline").a
article_text = article_tag.get_text()
article_link = article_tag.get("href")
article_upvote = soup.find(id="score_40247604").getText()

article_links, article_texts = [], []

for i in soup.find_all(name="span", class_="titleline"):
    article_links.append(i.a.get("href"))
    article_texts.append(i.getText())
    
article_upvotes = [int(a.get_text().split()[0]) for a in soup.find_all(name="span", class_="score")]

highest_upvote = -1
highest_upvote_index = -1
for index in range(len(article_upvotes)):
    if article_upvotes[index] > highest_upvote:
        highest_upvote_index = index

#####################
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_links[largest_index])
print(article_texts[largest_index])
print(article_upvotes[largest_index])
####################
