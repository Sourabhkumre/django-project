from django.shortcuts import render
from .models import Attendance


def attendance_list(request):

    attendance = Attendance.objects.all()

    return render(
        request,
        'attendance/list.html',
        {'attendance': attendance}
    )