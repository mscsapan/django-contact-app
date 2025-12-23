from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from utils.helper import get_specific_fields,get_all_items_with_fields,get_single_item_with_fields
from . models import Contact


# Create your views here.
def home(request):
    contacts = Contact.objects.all()
    return render(request,'index.html',context={'contacts': contacts})


def add_contact(request):
    return render(request,'add_contact_form.html')

def show_contact(request,id):
    contact = get_object_or_404(Contact,pk=id)
    return render(request,'view_contact.html',{'contact':contact})

def update_contact(request,id):
    contact = get_object_or_404(Contact,pk=id)
    return render(request,'update_contact_form.html',{'contact':contact})