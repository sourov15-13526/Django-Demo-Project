from django.http import HttpResponse
from django.shortcuts import render

from About_Us.models import Teacher

# Create your views here.
def about_us(request):
    return render(request,'about/about.html')

def teachers_info(request):
    teach = Teacher.objects.all()
    
    return render(request, 'about/table.html', {'thr' : teach})
    
