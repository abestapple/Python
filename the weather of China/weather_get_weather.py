#__*__ encoding:utf-8 __*__
from database import Code,db
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
headers={"User-Agent":UserAgent().chrome}
# url="http://www.weather.com.cn/weather/101090107.shtml"
# urls="http://www.weather.com.cn/weather/101010200.shtml"
def get_weather_condition(url):
    res=requests.get(url,headers=headers)
    res.encoding="utf-8"
    soup=BeautifulSoup(res.text,"lxml")
    data=soup.select(".crumbs")[0]
    #province=data.select("a")[0].text
    goal = data.select("span")[-1].text
    #天气预报的地址
    address = "%s" % goal
    #print(address)
    times=soup.select(".t li h1")
    #print(times)
    weath=soup.select(".wea")
    #print(weath)
    temperature=soup.select(".tem")
    #print(temperature)
    #dwind=soup.select(".win em span")
    #print(dwind)
    wind=soup.select(".win i")
    #print(wind)
    for i in range(0,len(times)-1):
        data="%s:\n时间：%s\n天气状况:%s\n温度:%s风级:%s\n"%(address,times[i].text,weath[i].text,temperature[i].text,wind[i].text)
        print(data)

# code=Code.query.filter(Code.code==101160101).first()
message=input("地名:")
try:
    me=Code.query.filter(Code.city==message).first()
    code=me.code
    url="http://www.weather.com.cn/weather/{}.shtml".format(code)
    get_weather_condition(url)
except:
    print("地名不对啊")