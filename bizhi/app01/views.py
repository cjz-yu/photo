from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def base(request):
    return render(request,"base.html")
def login(request):
    return render(request,"login.html")
def downloads(request):
    return render(request,"downloads.html")

#################################################################

from django.views import View
import logging
from .forms import LoginForm
logger = logging.getLogger("account")
from django.shortcuts import render, HttpResponse,redirect,reverse
from django.contrib.auth.hashers import check_password as auth_check_password
# class Login(View):
#     def get(self, request):
#         # 设置下一跳转地址(如果get有next，如果没有跳转到repo:index)
#         # request.session["next"] = request.GET.get('next', reverse('repo:index'))
#         # 如果已登录，则直接跳转到index页面
#         # request.user 表示的是当前登录的用户对象,没有登录 `匿名用户`
#         # if request.user.is_authenticated:
#         #     return redirect(request.session["next"])
#         form = LoginForm()
#         return render(request, "login.html", {"form": form})
#     # Form表单直接提交
#     # def post(self, request):
#     #     # 表单数据绑定
#     #     form = LoginForm(request.POST)
#     #     if form.is_valid():
#     #         username = form.cleaned_data["username"]
#     #         captcha = form.cleaned_data["captcha"]
#     #         session_captcha_code = request.session.get("captcha_code", "")
#     #         logger.debug(f"登录提交验证码:{captcha}-{session_captcha_code}")
#     #         # 验证码一致
#     #         if captcha.lower() == session_captcha_code.lower():
#     #             user, flag = form.check_password()
#     #             # user = auth.authenticate(username=username, password=password)
#     #             if user is not None and user.is_active:
#     #                 auth.login(request, user)
#     #                 logger.info(f"{user.username}登录成功")
#     #                 # 跳转到next
#     #                 return redirect(request.session.get("next", '/'))
#     #             msg = "用户名或密码错误"
#     #             logger.error(f"{username}登录失败, 用户名或密码错误")
#     #         else:
#     #             msg = "验证码错误"
#     #             logger.error(f"{username}登录失败, 验证码错误")
#     #     else:
#     #         msg = "表单数据不完整"
#     #         logger.error(msg)
#     #     return render(request, "login.html", {"form": form, "msg": msg})
