
import requests
from bs4 import BeautifulSoup

# url = "https://www.example.com"
# res = requests.get(url,timeout=10)

#print(res.status_code)
#print(res.text)

# soup = BeautifulSoup(res.text,"html.parser")
# res1 = soup.find_all("a")

# for link in res1:
#     print("Text ",link.text)
#     print("URL ",link.get("href"))

#print(soup.title)
#print(soup.title.text)

# html = """
# <h1>hello world</h1>
# <p>text1</p>
# <p>text2</p>
# <a href="https://www.google.com">Google</a>
# <a href="https://www.youtube.com">youtube</a>
# <a href="https://www.github.com">github</a>
# """

# soup1 = BeautifulSoup(html,"html.parser")
# res1 = soup1.find("p")
# res2 = soup1.find_all("p")

# print(res1)
# print(res1.text)

#print(res2)
#print(res2.text) -> gets an error because res2 store [<p>text1</p><p>text2</p>] as list of objects so we need to go through each element

# for p in res2:
#     print(p)
#     print(p.text)

# res3 = soup1.find_all("a")

# for p in res3:
#     print(p)
#     print(p.text)
#     print(p.get("href"))

# with open("index.html","r",encoding="utf-8") as file:
#     html_content = file.read()
#     soup = BeautifulSoup(html_content,"html.parser")
#     res4 = soup.find("p")
#     print(res4.text)

# day 29/7/26

# html = """
# <div id="box">
# <h2 class="heading">News</h2>
# <p class="content">Today is sunny</p>
# <p class="content">Tomorrow is runny</p>
# </div>
# """

# soup = BeautifulSoup(html,"html.parser")
# res = soup.find("h2")
# print(res.text)
# res1 = soup.find_all("p")
# for p in res1:
#     print(p.text)
# res4 = soup.find_all("div")
# for q in res4:
#     print(q.text)
# print("task1")
# res = soup.find(id="box")
# print(res.text)
# print("task2")
# res1 = soup.find(class_="heading")
# print(res1.text)
# print("task3")
# res2 = soup.find_all(class_="content")
# for p in res2:
#     print(p.text)

#css selectors(select() and select_one())
#select() -> returns all matching elements
# soup = BeautifulSoup(html,"html.parser")
# res = soup.select("p")
# print("task1")
# for p in res:
#     print(p.text)
# print("task2")
# res1= soup.select_one("h2")
# print(res1.text)
# print("task3")
# res3 = soup.select("#box")
# for j in res3:
#     print(j.text)

# html ="""
# <html>
# <body>
#    <div id="box">
#        <h2>News</h2>
#        <p class="content">Today is sunny</p>
#        <p class="content">Tomorrow is runny</p>
#    </div>
# </body>
# </html>
# """

# soup = BeautifulSoup(html,"html.parser")
# res = soup.find("p")
# print(res.parent.name)
# # res1 = soup.find("div")
# div = soup.find("div")
# for i in div.children:
#     if i.name:
#         print(i.name)

# siblings
# res = soup.find("p")
# print(res.find_previous_sibling().text)
# print(res.find_next_sibling().text)

url = "https://quotes.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")
print(res.status_code)
print(soup.title.text)
quotes = soup.find_all(class_="quote")
for q in quotes:
    text = q.find(class_="text").text
    author = q.find(class_="author").text
    print(text)
    print(author)
    tags = soup.find_all(class_="tag")
    for tag in tags:
        print(tag.text)
    print("*"*40)


