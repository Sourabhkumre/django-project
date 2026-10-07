from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views as account_views
from students import views as student_views
from teachers import views as teacher_views
from courses import views as course_views
from attendance import views as attendance_views
from results import views as result_views
from notices import views as notice_views


urlpatterns = [

    path('admin/', admin.site.urls),

    # Home
    path('', account_views.home, name='home'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard
    path('dashboard/', account_views.dashboard, name='dashboard'),

    # Students
    path('students/', student_views.student_list, name='students'),

    # Teachers
    path('teachers/', teacher_views.teacher_list, name='teachers'),

    # Courses
    path('courses/', course_views.course_list, name='courses'),

    # Attendance
    path('attendance/', attendance_views.attendance_list, name='attendance'),

    # Results
    path('results/', result_views.result_list, name='results'),

    # Notices
    path('notices/', notice_views.notice_list, name='notices'),
]