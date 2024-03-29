"""bizhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls import url, include
from bizhi.settings import MEDIA_ROOT
from django.views.static import serve

from django.views.generic import TemplateView
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # url(r'^index/$', views.index),
    # url(r'^base/$',views.base),
    url(r'^picture/',include('apps.picture.urls',namespace="picture") ),
    url(r'^accounts/',include('apps.accounts.urls',namespace="accounts") ),
    url(r'^apis/', include('apps.apis.urls', namespace="apis")),
    url(r'^uc/', include('apps.usercenter.urls', namespace="uc")),
    url(r'^test/$', views.test, name="test"),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^$', TemplateView.as_view(template_name='single-item.html')),

]

