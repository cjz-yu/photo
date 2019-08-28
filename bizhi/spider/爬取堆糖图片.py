import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bizhi.settings")  # website可以更改为自己的项目名称
django.setup()
from apps.picture.models import Picture,Category
from apps.accounts.models import User
import json
import requests,time
url="https://www.duitang.com/napi/blog/list/by_search/?kw={}&type=feed&include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id&_type=&start={}&_=1537966313841"
lamb = "民谣"
for index in range(0,240,24):
    #print(index)
    u = url.format(lamb,index)
    response = requests.get(u)
    html = response.text
    data = json.loads(html)
    time.sleep(3)
    for i in range(len(data["data"]["object_list"])):
        picture_url = data["data"]["object_list"][i]["photo"]["path"]                #(图片url)
        count = data["data"]["object_list"][i]["like_count"]                  #(收藏数)
        picture_name = data["data"]["object_list"][i]["album"]["name"]       # （图片名称）
        username = data["data"]["object_list"][i]["sender"]["username"]   #（上传人的用户名）
        avator_sor = data["data"]["object_list"][i]["sender"]["avatar"]    #（上传人的头像）
        tag = data["data"]["object_list"][i]["msg"]
        print(picture_name,picture_url,username,avator_sor,count,tag)#(图片标签)
        user = User.objects.get_or_create(username=username, avator_sor=avator_sor)
        p = Picture.objects.create(picture_name=picture_name,picture_url=picture_url,count=count,contributor_id=user[0].id)
        p.save()
