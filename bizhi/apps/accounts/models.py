from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# 继承自AbstractUser
class User(AbstractUser):
    # 如果定制User，需要在Settings配置AUTH_USER_MODEL
    # CharField => max_length
    # ImageFiled => Pillow 库
    realname = models.CharField(max_length=8, verbose_name="真实姓名",null=True)
    mobile = models.CharField(max_length=11, verbose_name="手机号",null=True)
    qq = models.CharField(max_length=11, verbose_name="QQ号",null=True)
    email = models.EmailField(verbose_name="邮箱",null=True)
    avator_sor = models.ImageField(upload_to="avator/%Y%m%d/", default="avator/default.jpg", verbose_name="头像")
