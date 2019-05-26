from django.shortcuts import render
from .models import Course

def index(request):
    courses = Course.objects.find()
    context = {'courses': courses}

    return render(request, 'courses/index.html', context)
