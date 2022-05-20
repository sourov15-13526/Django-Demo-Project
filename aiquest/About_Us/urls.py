from django.urls import path
from . import views

urlpatterns = [
    path('',views.about_us, name='about'),
    path('t/',views.teachers_info)
]