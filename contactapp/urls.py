from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add-contact/',views.add_contact, name='add-contact'),
    path('save-contact/',views.save_contact, name='save-contact'),
    path('show-contact/<int:id>',views.show_contact, name='show-contact'),
    path('update-contact/<int:id>',views.update_contact, name='update-contact'),
]
