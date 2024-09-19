import urllib.request
import urllib.parse
from ast import parse

api = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

station_id = input("지역 코드를 입력하세요 : ")
values = {'stnId':station_id}

url = api + '?' +