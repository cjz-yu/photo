import requests
from lxml import etree

from bs4 import BeautifulSoup

j=1
for i in range(1):
    url = "https://www.fabiaoqing.com/search/search/keyword/{}"
    url=url.format(i+1)
    html = requests.get(url)
    html=html.text
    soup = BeautifulSoup(html, "lxml")
    img = soup.select(".searchbqppdiv > a > img")
    for i in img:
        j=j+1
        print(j)
        photo=i["data-original"]
        url=requests.get(photo)
        print(url.text)
        # photo = url.()
        # print(photo)
        # with open("photo{i}.jpg","w+") as f:
        #     f.write(photo)
        #     print(i["data-original"])