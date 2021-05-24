import requests
from bs4 import BeautifulSoup

html = requests.get('https://open.spotify.com/playlist/37i9dQZF1DX8NzI27ip7J0')
#將此頁面的HTML GET下來

soup = BeautifulSoup(html.text,"html.parser") #將網頁資料以html.parser
print(soup.prettify())

song = []
for i in soup.find_all("span", class_="track-name"):
    print(i.text)
    song.append(i.text)

group = []
for i in soup.body.find_all("span"):
    x = i.find_all("a")
    if x != []:
        for j in x:
            if x.index(j) == 0:
                y = j.find_all("span")
                for l in y:
                    group.append(l.text)
                    print(l.text)

title = soup.head.title
print(title.text)
for i in range(len(song)):
    print(f'{i+1:2d}.  {group[i]:15s}{song[i]:15s}')
