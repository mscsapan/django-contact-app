from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')


def add_contact(request):
    return render(request,'form.html')

def edit_contact(request,id):
    return render(request,'show.html')