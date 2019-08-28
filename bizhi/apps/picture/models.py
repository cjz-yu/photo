from django.db import models
from apps.accounts.models import User
# Create your models here.
class Category(models.Model):
    """标签"""
    name = models.CharField("标签名", max_length=64)
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"

class Picture(models.Model):
    picture_url = models.CharField(max_length=100,verbose_name="图片地址")
    photo_url = models.CharField(max_length=100,verbose_name="图片本地地址")

    picture_name = models.CharField(max_length=100,verbose_name="图片名字", null=True)
    category = models.ManyToManyField(Category, verbose_name="所属分类",null=True)
    contributor = models.ForeignKey(User, verbose_name="贡献者", null=True)
    status = models.BooleanField("审核状态", default=False)
    pub_time = models.DateTimeField("入库时间", auto_now_add=True, null=True)
    count=models.IntegerField("图片浏览数",null=True)
    class Meta:
        verbose_name = "图片表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return f"{self.id}:{self.picture_url}"

class Comment(models.Model):
    photo = models.ForeignKey(Picture, verbose_name="图片")
    user = models.ForeignKey(User, verbose_name="评论人")
    content = models.TextField(verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "图片评论表"
        verbose_name_plural = verbose_name
        # 定义权限 => auth_permission表插入数据
        permissions = (
            ('can_change_question', "可以修改图片信息"),
            ('can_add_question', "可以添加图片信息"),
            ('can_change_question_status', '可以修改图片状态'),
        )

    def __str__(self):
        return f"{self.id}:{self.photo.contributor}"
