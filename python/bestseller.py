import requests
from bs4 import BeautifulSoup

# 예스24 베스트셀러 페이지 URL
url = "http://www.yes24.com/24/Category/BestSeller"
headers = {'User-Agent': 'Mozilla/5.0'}

# 웹 페이지 요청 및 파싱
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 책 제목 정보 추출
books = soup.select('ol > li > div > div > div.info > a.gd_name')[:10]

# 각 책 제목 출력
for i, book in enumerate(books, 1):
    print(f"{i}. {book.text.strip()}")