from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # contents = ['Mohammad','Ali','Khan','Baba','Ibrahim','Hanzala']
    contents = [
        {
        'id': 1,
        'first_name':'Mohammad',
        'last_name':'Ali',
        'phone':'018829281',
        'email':'mscsapan@gmail.com'
        },
        {
        'id': 2,
        'first_name':'Khan',
        'last_name':'Baba',
        'phone':'02921829281',
        'email':'khan.baba@gmail.com'
        },
         {
        'id': 3,
        'first_name':'Ibrahim',
        'last_name':'BKhan',
        'phone':'9888726',
        'email':'ibrahim@gmail.com'
        },
    ]
    return render(request,'index.html',context={'contents': contents})


def add_contact(request):
    return render(request,'add_contact.html')

def edit_contact(request,id):
    return render(request,'view_contact.html')