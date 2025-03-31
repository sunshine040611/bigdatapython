import requests
from bs4 import BeautifulSoup

# 멜론 차트 URL
url = "https://www.melon.com/chart/index.htm"

# HTTP GET 요청을 보내고 웹 페이지 내용을 가져옵니다.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

# 웹 페이지의 내용을 파싱합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 노래와 아티스트 정보를 추출합니다.
songs = soup.select('div.ellipsis.rank01 a')
artists = soup.select('div.ellipsis.rank02 a')

# 결과 출력
for idx, (song, artist) in enumerate(zip(songs, artists), 1):
    print(f"{idx}. {song.text} - {artist.text}")


import random
import time
for song in songs:
    print(song)

print ("AI야 노래 한곡만 추천해줘")
print ("알겠습니다.")
# 멜론 차트 100중에서 노래 한 곡 추천해주는 서비스 만들기기
ai_song = random.choice(songs)
dd=["두","두","두둥"]
for d in dd:
    print(d)
    time.sleep(1)
print (f"제가 추천한 곡은 {ai_song}입니다.")
