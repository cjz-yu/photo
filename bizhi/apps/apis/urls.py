from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'^get_mobile_captcha/$', views.get_mobile_captcha, name='get_mobile_captcha'),
    url(r'^change_avator/$', views.ChangeAvator.as_view(), name='change_avator'),

]