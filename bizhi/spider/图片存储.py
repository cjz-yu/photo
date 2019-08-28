import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bizhi.settings")  # website可以更改为自己的项目名称
django.setup()
import json
import requests,time
from apps.picture.models import User
url="https://www.duitang.com/napi/blog/list/by_search/?kw={}&type=feed&include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id&_type=&start={}&_=1537966313841"
lamb = "女孩"
k=0
j=0
for index in range(0,2400,24):
    u = url.format(lamb,index)
    response = requests.get(u)
    html = response.text
    data = json.loads(html)
    time.sleep(1)
    j = j+k
    for i in range(len(data["data"]["object_list"])):
        avator_sor = data["data"]["object_list"][i]["sender"]["avatar"]    #（上传人的头像）
        photo=requests.get(avator_sor).content
        os.chdir(r"D:\git仓库\photo\question_bank\bizhi\media\avator")
        p = User.objects.get(id=i+j+131)
        filename = avator_sor.split("/")[-1]
        print(i)
        k = len(data["data"]["object_list"])
        time.sleep(0.5)
        with open(filename,"wb") as  f:
            f.write(photo)
            p.avator_sor = f"/media/avator/{filename}"
            p.save()
            print("数据库录入成功")
            # avator_sor = data["data"]["object_list"][i]["sender"]["avatar"]    #（上传人的头像）
        # print(picture_url,avator_sor)
