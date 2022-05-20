from django.urls import path
from . import views

urlpatterns = [
    path('ml/',views.machine_Learning, name='machine'),
    path('random/',views.random, name='random'),
    path('knn/',views.k_nearest, name='knn'),
    path('dt/',views.dtree, name='dtree'),
]