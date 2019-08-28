from django.shortcuts import render,reverse,redirect
from .forms import LoginForm,RegisterForm
from django.views import View
from django.contrib import auth
import logging
logger = logging.getLogger("accounts")

# Create your views here.
class Login(View):
    def get(self, request):
        # 设置下一跳转地址(如果get有next，如果没有跳转到repo:index)
        request.session["next"] = request.GET.get('next', reverse('accounts:index'))
        # 如果已登录，则直接跳转到index页面
        # request.user 表示的是当前登录的用户对象,没有登录 `匿名用户`
        if request.user.is_authenticated:
            return redirect(request.session["next"])
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    def post(self, request):
        # 表单数据绑定
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            captcha = form.cleaned_data["captcha"]
            session_captcha_code = request.session.get("captcha_code", "")
            logger.debug(f"登录提交验证码:{captcha}-{session_captcha_code}")
            # 验证码一致
            # print(captcha.lower(), session_captcha_code.lower())
            if captcha.lower() == session_captcha_code.lower():
                user, flag = form.check_password()
                # user = auth.authenticate(username=username, password=password)
                if flag and user and user.is_active:
                    auth.login(request, user)
                    logger.info(f"{user.username}登录成功")
                    # 跳转到next
                    return redirect(request.session.get("next", '/'))
                msg = "用户名或密码错误"
                logger.error(f"{username}登录失败, 用户名或密码错误")
            else:
                msg = "验证码错误"
                logger.error(f"{username}登录失败, 验证码错误")
        else:
            msg = "表单数据不完整"
            print(form.errors)
            # logger.error(msg)
        return render(request, "login.html", {"form": form, "msg": msg})

from django.core.cache import cache
from .models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form":form})
    def post(self, request):
        ret = {"status": 400, "msg": "调用方式错误"}
        # 检查是不是ajax的请求
        print(1)
        if request.is_ajax():
            form = RegisterForm(request.POST)
            print(2)
            if form.is_valid():
                print(3)
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                mobile = form.cleaned_data["mobile"]
                email = form.cleaned_data["email"]
                mobile_captcha = form.cleaned_data["mobile_captcha"]
                mobile_captcha_reids = cache.get(mobile)
                if mobile_captcha == mobile_captcha_reids:
                    user = User.objects.create(username=username, password=make_password(password))
                    user.save()
                    ret['status'] = 200
                    ret['msg'] = "注册成功"
                    logger.debug(f"新用户{user}注册成功！")
                    user = auth.authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        logger.debug(f"新用户{user}登录成功")
                    else:
                        logger.error(f"新用户{user}登录失败")
                else:
                    # 验证码错误
                    ret['status'] = 401
                    ret['msg'] = "验证码错误或过期"
            else:
                ret['status'] = 402
                ret['msg'] = form.errors
            logger.debug(f"用户注册结果：{ret}")
        return JsonResponse(ret)
from django.contrib.auth.decorators import login_required
@login_required()
def index(request):
    return redirect(reverse("picture:show"))

def logout(request):
    auth.logout(request)
    return redirect(reverse("accounts:login"))
from django.contrib.auth.decorators import login_required
