import requests
from datetime import datetime
import pandas as pd


date = datetime.now().strftime('%Y%m%d')
attraction_list = pd.read_excel('C:/MG/attraction_list.xlsx')
# weather_grid = pd.read_excel('C:/MG/weather_grid.xlsx')


attraction_keyword = input()
attraction = attraction_list[attraction_list['장소'].str.contains(attraction_keyword)]
attraction_location = list(attraction['위치'].str.split(' '))
sidoName = attraction_location[0][0]
for i in range(len(attraction_location[0])):
    if attraction_location[0][i][-1] in ['동', '면', '읍']:
        umdName = attraction_location[0][i]
        break
    else:
        umdName = attraction_location[0][-2]

url_station = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getNearbyMsrstnList'
url_tmXY = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getTMStdrCrdnt'

payload_tmXY = {
    'serviceKey' : '---',
    'returnType' : 'JSON',
    'umdName' : umdName
}

t_res = requests.get(url_tmXY, params=payload_tmXY)
tmXY_dict = t_res.json()['response']['body']['items']
tmXY = [item for item in tmXY_dict if item['sidoName'] == sidoName][0]

tmX = tmXY['tmX']
tmY = tmXY['tmY']

if sidoName == '경상남도':
    sidoName = '경남'
elif sidoName == '경상북도':
    sidoName = '경북'
elif sidoName == '전라남도':
    sidoName = '전남'
elif sidoName == '전라북도':
    sidoName = '전북'
elif sidoName == '충청남도':
    sidoName = '충남'
elif sidoName == '충청북도':
    sidoName = '충북'
else:
    sidoName = sidoName[0:2]

payload_station = {
    'serviceKey' : '---',
    'returnType' : 'JSON',
    'tmX' : tmX,
    'tmY' : tmY
}

s_res = requests.get(url_station, params=payload_station)
stationName = s_res.json()['response']['body']['items'][0]['stationName']  # 요청한 TM 좌표로부터 가장 짧은 거리의 측정소 선택

url_weather = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
url_dust = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

payload_weather = {
    'ServiceKey' : '---',
    'pageNo' : '1',
    'numOfRows' : '13',
    'dataType' : 'JSON',
    'base_date' : date,
    'base_time' : '0200',
    'nx' : '10',
    'ny' : '15' }

payload_dust = {
    'serviceKey' : '---',
    'returnType' : 'JSON',
    'numOfRows' : '100',
    'pageNo' : '1',
    'sidoName' : sidoName,
    'ver' : '1.0'
}

w_res = requests.get(url_weather, params=payload_weather)
weather_dict = w_res.json()['response']['body']['items']['item']

d_res = requests.get(url_dust, params=payload_dust)
dust_dict = d_res.json()['response']['body']['items']


attraction_dust = [item for item in dust_dict if item['stationName'] == stationName]
attraction_pm10 = attraction_dust[0]['pm10Value']+'㎍/㎥'
attraction_pm25 = attraction_dust[0]['pm25Value']+'㎍/㎥'


for i in range(len(weather_dict)):
    # 강수확률
    if weather_dict[i]['category'] == 'POP':
        rain_prob = weather_dict[i]['fcstValue'] + '%'
    # 하늘상태
    elif weather_dict[i]['category'] == 'SKY':
        if weather_dict[i]['fcstValue'] == '1':
            sky = '맑음'
        elif weather_dict[i]['fcstValue'] == '3':
            sky = '구름많음'
        else:
            sky = '흐림'
    # 강수형태
    elif weather_dict[i]['category'] == 'PTY':
        if weather_dict[i]['fcstValue'] == '0':
            rain_type = '없음'
        elif weather_dict[i]['fcstValue'] == '1':
            rain_type = '비'
        elif weather_dict[i]['fcstValue'] == '2':
            rain_type = '비/눈'
        elif weather_dict[i]['fcstValue'] == '3':
            rain_type = '눈'
        elif weather_dict[i]['fcstValue'] == '4':
            rain_type = '소나기'
        elif weather_dict[i]['fcstValue'] == '5':
            rain_type = '빗방울'
        elif weather_dict[i]['fcstValue'] == '6':
            rain_type = '빗방울/눈날림'
        elif weather_dict[i]['fcstValue'] == '7':
            rain_type = '눈날림'
    # 3시간 기온
    elif weather_dict[i]['category'] == 'T3H':
        temperature = weather_dict[i]['fcstValue'] + '℃'

print(attraction_keyword+'의 날씨 정보', '\n',
      '강수확률:', rain_prob, '\n', '강수형태:', rain_type, '\n', '하늘상태:', sky, '\n', '기온:', temperature, '\n',
      '미세먼지:', attraction_pm10, '\n', '초미세먼지:', attraction_pm25)
