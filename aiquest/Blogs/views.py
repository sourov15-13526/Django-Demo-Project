from django.http import HttpResponse
from django.shortcuts import render

from Blogs.forms import TeachersRegistration

# Create your views here.
def blog1(request):
    return render(request,"blogs/blog.html")

def showformsdata(request):
    if request.method == "POST":
        fm = TeachersRegistration(request.POST)
        if fm.is_valid():
            print('This is Post method')
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
        
    else:
        fm = TeachersRegistration()
        print('This is GET method')
    
    #fm.order_fields(field_order=['first_name','last_name','email','password','textarea'])
    return render(request, 'blogs/forms.html', {'form': fm})
