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