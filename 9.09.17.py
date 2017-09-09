import urllib.request  # импортируем модуль
import re

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
req = urllib.request.Request('https://yandex.ru/pogoda/moscow', headers={'User-Agent':user_agent})

with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')

regweather = re.compile('<span class="current-weather__comment">(.*?)</span>', flags= re.DOTALL)
regtemp = re.compile('<div class="current-weather__thermometer current-weather__thermometer_type_now">(.*?)</div>')
weather = re.search(regweather, html).group(1)
temp = re.search(regtemp, html).group(1)
print('Погода в Москве сейчас:', weather, ',', temp)

##new_weather = []
##regTag = re.compile('<.*?>', re.DOTALL)
##regSpace = re.compile('\s{2,}', re.DOTALL)
##for t in titles:
##    clean_t = regSpace.sub("", t)
##    clean_t = regTag.sub("", clean_t)
##    new_titles.append(clean_t)
##for t in new_titles:
##    print(t)
