from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_Learning(request):
    course = 'machine learning'
    Tclass = 21
    seat = 20
    cduration = '2.5 months'
    offering = {'c':course, 'tl':Tclass, 'st':seat, 'cd':cduration}
    Teachers = {'Names':['Shakil', 'Mijbah', 'Suhanur']}
    return render(request, 'machine_learning/machine_learning.html', context=Teachers)

def random(request):
    return render(request, 'machine_learning/random_forest.html')

def k_nearest(request):
    return render(request, 'machine_learning/knn.html')

def dtree(request):
    return render(request, 'machine_learning/DT.html')

