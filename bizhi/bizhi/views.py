import logging
from django.shortcuts import HttpResponse,render

# apis为settings中Logging配置中的loggers
logger = logging.getLogger('apis')


def test(request):
    return render(request,'index1.html')