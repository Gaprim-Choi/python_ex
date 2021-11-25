import glob
import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100/"

html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, "lxml")

titles = soup_music.select('h3.a-no-trucate')
print(titles[0:7])

music_titles = [title.get_text().strip() for title in titles]
print(music_titles[0:7])

artists = soup_music.select('span.a-no-trucate')
print(artists[0:7])

""" artists = soup_music.select('span.a-no-trucate')
print(artists[0:7]) """
music_artists = [artists.get_text().strip() for artists in artists]
print(music_artists[0:7])

for k in range(7):
    print("{0}: {1} / {2}".format(k+1, music_titles[k], music_artists[k]))

music_titles_artists = {}
order = 0

for (music_title, music_artist) in zip(music_titles, music_artists):
    order = order + 1
    music_titles_artists[order] = [music_title, music_artist]

print(music_titles_artists[1])

file_name = './ch17_webscraping/billboard_top100.txt'

f = open(file_name, 'w', encoding="utf-8")

for k in range(len(music_titles_artists)):
    f.write("{0:2d}: {1}/{2}\n".format(k+1,
                                       music_titles[k],  music_artists[k]))

f.close()  # 파일 닫기

glob.glob(file_name)  # 생성된 파일 확인