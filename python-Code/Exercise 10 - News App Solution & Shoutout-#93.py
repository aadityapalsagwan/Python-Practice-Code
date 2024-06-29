# Exercise 10 - News App Solution & Shoutout.......

import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}tesla&from=2023-12-15&sortBy=publishedAt&apiKey=0949473df55b4f65b1e510063065973b"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")

