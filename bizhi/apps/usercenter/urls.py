from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^edit_account/$', views.Edit_account.as_view(), name="edit_account"),
    # # 修改密码个人资料
    # url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    # url(r'^change_passwd/$', views.ChangePasswdView.as_view(), name='change_passwd'),
    # #　我的回答
    # url(r'^answer/$', views.test, name='answer'),
    # # 我的收藏
    # url(r'^collect/$', views.test, name='collect'),
    # # 我的贡献
    # url(r'^contribut/$', views.test, name='contribut'),
    # # 待审题目
    # # url(r'^approval/$', views.test, name='approval'),
    # url(r'^approval/$', views.ApprovalView.as_view(), name='approval'),
    # # 审核题目
    # url(r'^approval/(?P<id>\d+)/$', views.ApprovalPassView.as_view(), name='approval_pass'),
    # url(r'^approval/id/$', views.test, name='approval_pass'),
    url(r'^ttt/$', TemplateView.as_view(template_name="uc_base.html"),name="ttt" ),


]