from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Picture,User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

class Picutuelist(LoginRequiredMixin,ListView):
    def get(self, request):
        photo_list = Picture.objects.all().order_by("id")
    # user_list = User.objects.all()
        paginator = Paginator(photo_list, 20) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'index.html', {'contacts': contacts})
    def get_context_data(self, **kwargs):
        photo_list = Picture.objects.all().order_by("id")
        paginator = Paginator(photo_list, 20) # Show 25 contacts per page
        context = super(Picutuelist, self).get_context_data(**kwargs)
        paginator_data = self.get_pagination_data(paginator,page_obj=context)
        context.update(paginator_data)  # 将当前字典的kv更新到context字典中。
        return context

# 　　 <br>  # 这里来负责跳转的页码处理

    def get_pagination_data(self, paginator, page_obj, around_count=2):  # arount_count=2表示从当前页前推两页，后推两页
        current_page = page_obj.number
        num_page = paginator.num_pages

        left_has_more = False  # 左边还有没有未显示的页码
        right_has_more = False
        if current_page <= around_count + 2:
            left_page = range(1, current_page)
        else:
            left_has_more = True
            left_page = range(current_page - around_count, current_page)
        if current_page >= num_page - around_count - 1:
            right_page = range(current_page + 1, num_page + 1)
        else:
            right_has_more = True
            right_page = range(current_page + 1, current_page + 3)
        return {
            'left_pages': left_page,
            'right_pages': right_page,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
        }
# Create your views here.
