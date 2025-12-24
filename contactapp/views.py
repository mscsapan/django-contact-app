import json
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.helper import debug_item
from . models import Contact


# Create your views here.
def home(request):
    contacts = Contact.objects.all()
    return render(request,'index.html',context={'contacts': contacts})


def add_contact(request):
    return render(request,'add_contact_form.html')


@csrf_exempt
def save_contact(request):
   try:
       if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            
            contact = Contact(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address)
            print(f'dataaaaaa {contact.objects.all()}')
            data = json.loads(request.body)
            return JsonResponse(data,safe=False)
         
   except Exception as e:
        return JsonResponse({"error": str(e)}, status=405)

# @csrf_exempt
# def save_contact(request):
#     """Save and return JSON"""
#     if request.method == 'POST':
        
#         contact = Contact.objects.create(
#             first_name=request.POST.get('first_name'),
#             last_name=request.POST.get('last_name'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             address=request.POST.get('address')
#         )
        
#         data = get_single_item(Contact, contact.id)
        
#         return JsonResponse({
#             "success": True,
#             "message": "Contact saved!",
#             "data": data
#         }, status=201)
    
#     return JsonResponse({"error": "POST required"}, status=405)

def show_contact(request,id):
    contact = get_object_or_404(Contact,pk=id)
    return render(request,'view_contact.html',{'contact':contact})

def update_contact(request,id):
    contact = get_object_or_404(Contact,pk=id)
    return render(request,'update_contact_form.html',{'contact':contact})