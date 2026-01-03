from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.helper import dump,get_all_model_data
from . models import Contact


# Create your views here.
def home(request):
    contacts = Contact.objects.all()
    return render(request,'index.html',context={'contacts': contacts})

@login_required(login_url='login-first')
def add_contact(request):
    return render(request,'add_contact_form.html')

# def save_contact(request):
#     if request.method == 'POST':
#         # এটি স্বয়ংক্রিয়ভাবে সব ইনপুট ডাটাকে ডিকশনারি বানিয়ে ফেলবে
#         all_data = request.POST.dict() 
        
#         # পাসওয়ার্ড বা সেনসিটিভ কিছু থাকলে তা বাদ দিয়ে দিতে পারেন
#         all_data.pop('csrfmiddlewaretoken', None) 
        
#         return JsonResponse(all_data)

def save_contact(request):
   try:
       if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            
            contact = Contact(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address)
            # return dump(contact)
            contact.save()
            return redirect('home')
         
   except Exception as e:
        return JsonResponse({"error": str(e)}, status=405)

def show_contact(request,id):
    contact = get_object_or_404(Contact,pk=id)
    return render(request,'view_contact.html',{'contact':contact})

def edit_contact(request,id):
    contact = get_object_or_404(Contact,pk=id)
    return render(request,'edit_contact_form.html',{'contact':contact})

def update_contact(request,id):
    try:
        if request.method == 'POST':
            contact = get_object_or_404(Contact,pk=id)
            
            contact.first_name = request.POST.get('first_name')
            contact.last_name = request.POST.get('last_name')
            contact.email = request.POST.get('email')
            contact.phone = request.POST.get('phone')
            contact.address = request.POST.get('address')
           
            # return dump(contact)
            contact.save()
            return redirect('home')
        
    except Exception as e:
        return JsonResponse({'Error': str(e)},status=403)
    
def delete_contact(request,id):
    contact = get_object_or_404(Contact,pk=id)
    contact.delete()
    return redirect('home')


def login(request):
    return render(request,'auth/auth.html')