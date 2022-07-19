from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



app_name="TechinalWeb"
urlpatterns = [
    path('<int:course_id>/',views.detail,name="Detail"),
    path('',views.Courses,name="Home-Page"),
    path('<int:course_id>/yourchoice/',views.yourchoice,name="yourchoice"),
    path('students/',views.student_list.as_view()),
    path('contact/',views.contact,name='contact'),
]