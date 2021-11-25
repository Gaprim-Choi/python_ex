import glob
import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100/"

html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, "lxml")

titles = soup_music.select('h3.a-no-trucate')
artists = soup_music.select('span.a-no-trucate')

music_titles = [title.get_text().strip() for title in titles]
music_artists = [artists.get_text().strip() for artists in artists]

file_name = './ch17_webscraping/billboard_top100.txt'

f = open(file_name, 'w', encoding="utf-8")

for k in range(len(music_titles)):
    f.write("{0:2d}: {1}/{2}\n".format(k+1,
                                       music_titles[k],  music_artists[k]))

f.close()  # 파일 닫기

glob.glob(file_name)  # 생성된 파일 확인