import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()
import requests
import random
from bs4 import BeautifulSoup


def set_conf():
    header_list = [
        # 遨游
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
        # 火狐
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
        # 谷歌
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"},
    ]
    proxy_ip = [{"http": "120.83.121.207:9999"},
                {"http": "163.204.242.159:9999"},
                {"http": "120.83.108.46:9999"},
                {"http": "163.204.247.120:9999"}]
    header = random.choice(header_list)
    proxy = random.choice(proxy_ip)
    print(header)
    print(proxy)
    return header


url = "https://www.fabiaoqing.com/search/search/keyword/2"

header = set_conf()
response = requests.get(url, headers=header)
html = response.text
# print(html)
soup = BeautifulSoup(html, "lxml")
img = soup.select(".searchbqppdiv > a > img")
for i in img:
    print(i["alt"])
    print(i["data-original"])
