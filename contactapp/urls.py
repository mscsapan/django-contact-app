from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add-contact/',views.add_contact, name='add-contact'),
    path('save-contact/',views.save_contact, name='save-contact'),
    path('show-contact/<int:id>',views.show_contact, name='show-contact'),
    path('edit-contact/<int:id>',views.edit_contact, name='edit-contact'),
    path('update-contact/<int:id>',views.update_contact, name='update-contact'),
    path('delete-contact/<int:id>',views.delete_contact, name='delete-contact'),
    
    path('login/',views.login_form, name='login'),
    path('signup/',views.signup_form , name='signup'),
    # path('user-login/',views.login_view, name='user-login'),
    # path('user-signup/',views.signup_view, name='user-signup'),
]
