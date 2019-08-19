from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$',views.Login.as_view(),name="login"),
    url(r'^register/$', views.Register.as_view(), name="register"),
    url(r'^index/$', views.index, name="index"),
    url(r'^logout/$', views.logout, name="logout"),

]