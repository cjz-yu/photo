# from django import forms
# from django.forms import widgets
# from django.core.exceptions import ValidationError
# from django.contrib.auth.hashers import check_password as auth_check_password
# class LoginForm(forms.Form):
#     username = forms.CharField(label="用户名", max_length="24",
#                                widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}))
#     captcha = forms.CharField(label="验证码", widget=widgets.TextInput(
#         attrs={"style": "width: 160px;padding: 10px", "placeholder": "验证码", "onblur": "check_captcha()",
#                "error_messages": {"invalid": "验证码错误"}}))
#     password = forms.CharField(label="密 码",
#                                widget=widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码"}))

    # def check_password(self):
    #     print('check password')
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     try:
    #         user = User.objects.get(username=username)
    #         return user, auth_check_password(password, user.password)
    #     except:
    #         return None, False
    #
    # def clean_username(self):
    #     print(self.cleaned_data.get("username"))
    #     ret = User.objects.filter(username=self.cleaned_data.get("username"))
    #     if ret:
    #         return self.cleaned_data.get("username")
    #     else:
    #         raise ValidationError("用户名或密码不正确")