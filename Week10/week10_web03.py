import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

shops = []

for i in range(1, 51):
    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
    # print(url)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        shops_name = tds[1].string
        shops_addr = tds[3].string
        shops_phone = tds[5].string

        shops.append([shops_name] + [shops_addr] + [shops_phone])

# print(shops)
hollys_df = pd.DataFrame(shops, columns = ('매장 이름', '주소', '전화 번호'));
hollys_df.to_csv('할리스 매장 목록.csv', mode='w', encoding='cp949')