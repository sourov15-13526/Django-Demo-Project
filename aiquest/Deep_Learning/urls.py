from django.urls import path
from . import views

urlpatterns = [
    path('',views.deep_learning, name='deep'),
    path('register/', views.registration)
]