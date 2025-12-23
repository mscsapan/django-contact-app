import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from utils.helper import get_specific_fields,get_all_items_with_fields,get_single_item_with_fields
from . models import Contact


# Create your views here.
def home(request):
    data = get_all_items_with_fields(Contact)
    return JsonResponse(data, safe=False, status=200)
  
    # return render(request,'index.html',context={'contents': contents})


def add_contact(request):
    return render(request,'add_contact.html')

def edit_contact(request,id):
    data = get_single_item_with_fields(model=Contact,id=id)
    return JsonResponse(data, safe=False, status=200)
    # return render(request,'view_contact.html')