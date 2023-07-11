import sqlite3
import requests
from bs4 import BeautifulSoup

url="https://books.toscrape.com/catalogue/category/books/history_32/index.html"
response=requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")
for book in books:
    # print(book.find('h3').find("a")["title"])
#    price=float(book.select(".price_color")[0].get_text().replace("£","").replace('Â',""))
   ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}  
   paragraph=book.select(".star-rating")[0]
   rating=paragraph.get_attribute_list("class")[-1]
   print(ratings[rating])

def getTitle(book):
   return book.find('h3').find("a")["title"]
def getPrice(book):
   return float(book.select(".price_color")[0].get_text().replace("£","").replace('Â',""))
def ratings(book):
   ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}  
   paragraph=book.select(".star-rating")[0]
   rating=paragraph.get_attribute_list("class")[-1]
   return ratings[rating]
   

# print(soup)