from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Picture,User
def listing(request):
    photo_list = Picture.objects.all()
    # user_list = User.objects.all()
    paginator = Paginator(photo_list, 25) # Show 25 contacts per page
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
# Create your views here.
