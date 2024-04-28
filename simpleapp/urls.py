# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome_page, name='welcome_page'),
    path('form/', views.first_form, name='first_form'),
    path('submit/', views.submit_form, name='submit_form'),
    path('form-success/', views.form_success, name='form_success'),  # Add this URL pattern
]
