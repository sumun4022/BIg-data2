import urllib.request
from idlelib.iomenu import encoding
import pandas as pd
from bs4 import BeautifulSoup
import datetime

# print(datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

shops = []

for i in range(1, 51):
    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
    # print(url)
    page = urllib.request.urlopen(url)          #특정 웹 페이지의 HTML을 가져온 후 page 변수에 저장
    soup = BeautifulSoup(page, "html.parser")       #page에 저장된 html을 파이썬으로 바꾸고 soup 변수에 저장
    tbody = soup.find('tbody')      #파싱된 html 객체에서 body태그를 찾고 body태그 안에 있는 모든 코드를 tbody 변수에 저장
    trs = tbody.find_all('tr')      #tbody안에 있는 코드에서 tr태그를 찾고 그 안에 있는 모든 코드를 리스트로 반환 후에 trs에 저장    

    for tr in trs:
        tds = tr.find_all('td')
        shops_name = tds[1].string
        shops_addr = tds[3].string
        shops_phone = tds[5].string

        shops.append([shops_name] + [shops_addr] + [shops_phone] + [datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")])

# print(shops)
hollys_df = pd.DataFrame(shops, columns = ('매장 이름', '주소', '전화 번호', '일시'))
hollys_df.to_csv('할리스 매장 목록.csv', mode='w', encoding='cp949')

# 인코딩 방식 중에서 메모장이나 엑셀에서는 cp949로 인코딩을 해야한다.
# 기본은 uft-8로 파이참에서 볼 수 있다.