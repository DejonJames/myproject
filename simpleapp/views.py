from django.http import HttpResponse
from django.shortcuts import redirect, render

def welcome_page(request):
    return render(request, 'welcome_page.html')

def first_form(request):
    return render(request, 'first_form.html')

def submit_form(request):
    if request.method == 'POST':
        # Process form data here
        return redirect('form_success')  # Redirect to the form success page
    else:
        return HttpResponse('Invalid request method')

def form_success(request):
    return render(request, 'form_success.html')