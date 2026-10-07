from django.shortcuts import render
from .models import Result


def result_list(request):

    results = Result.objects.all()

    return render(
        request,
        'results/list.html',
        {'results': results}
    )