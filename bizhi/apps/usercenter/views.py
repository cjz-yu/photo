from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

import logging
logger = logging.getLogger("account")

class Edit_account(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "edit-account.html")

    def post(self, request):
        ret_info = {"code": 200, "msg": "修改成功"}
        try:
            if request.POST.get("username"):
                request.user.username = request.POST.get("username")
            if request.POST.get("mobile"):
                print('change mobile')
                request.user.mobile = request.POST.get("mobile")
            if request.POST.get("qq"):
                request.user.qq = request.POST.get("qq")
            if request.POST.get("email"):
                request.user.email = request.POST.get("email")
            request.user.save()
        except Exception as ex:
            ret_info = {"code": 200, "msg": "修改失败"}
        print(ret_info)
        return render(request, "edit-account.html", {"ret_info":ret_info})
