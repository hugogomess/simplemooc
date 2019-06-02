from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.conf import settings

def register(request):
    template_name = 'registration/register.html'
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
        
    context = {
        'form': form
    }
    return render(request, template_name, context)


