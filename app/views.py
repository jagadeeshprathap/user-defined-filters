from django.shortcuts import render

# Create your views here.
def filter(request):
    d={'data':'hai HEllo i am JAGADEESh rrrr'}
    return render(request,'filter.html',d)