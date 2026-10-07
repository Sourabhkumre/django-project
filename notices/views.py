from django.shortcuts import render
from .models import Notice


def notice_list(request):

    notices = Notice.objects.all().order_by('-date')

    return render(
        request,
        'notices/list.html',
        {'notices': notices}
    )