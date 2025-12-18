from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add/',views.add_contact, name='add-contact'),
    path('edit/',views.home, name='home'),
]
