#__*__ encoding:utf-8 __*__
import requests,time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import queue,threading
city_name=[]
code=[]
from database import Code,db
#q=queue.Queue()
headers={"User-Agent":UserAgent().chrome}
start_url="http://www.weather.com.cn/textFC/hebei.shtml"
res=requests.get(start_url,headers=headers)
soup=BeautifulSoup(res.text, "lxml")
prov_urls=soup.select(".lqcontentBoxheader ul li a")
proverences_urls=[]
for i in prov_urls:
    proverences_urls.append("http://www.weather.com.cn"+i["href"])
    #q.put("http://www.weather.com.cn"+i["href"])
def get_city_code(url):
    res = requests.get(url, headers=headers)
    res.encoding="utf-8"
    soup = BeautifulSoup(res.text, "lxml")
    prov_urls = soup.select("td a")
    urls=prov_urls[0:-1:2]
    for i in urls:
        list=Code(city=i.text,code=i["href"].split("/")[-1].replace(".shtml", ""))
        db.session.add(list)
        db.session.commit()
#print(weather_city_code)
# url="http://www.weather.com.cn/textFC/beijing.shtml"
# get_city_code(url)

# start=time.time()
#
# for i in range(0,5):
#     url=q.get()
#     t=threading.Thread(target=get_city_code,args=(url,))
#     t.start()
# end=time.time()
a=0
# print(end-start)
for url in proverences_urls:
    get_city_code(url)
    print(a)
    a+=1
print("OK")