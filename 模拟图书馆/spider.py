#__*__ encoding:utf-8 __*__
import requests,queue,threading
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
q=queue.Queue()
from datebase import Book,db
headers={"User-Agent":UserAgent().chrome}

    # q.put(url)
def getmessage(url):
    res=requests.get(url,headers=headers)
    res.encoding="utf-8"
    soup=BeautifulSoup(res.text,"html.parser")
    btype=soup.select(".main-index a")[1].text
    data = soup.select(".cf li span")
    for i in data:
        name= i.select("a")[0].text
        author=i.select("a")[1].text
        mes=Book(name=name,author=author,btype=btype,num=8)
        db.session.add(mes)
        db.session.commit()
# for i in range(1,6):
#     a=q.get()
#     t=threading.Thread(target=getmessage,args=(a,))
#     t.start()
for i in range(1,12):
    url = "http://www.xs4.cc/list/%s_0.html"%i
    getmessage(url)
    print("yes")