from django.shortcuts import render, get_object_or_404
from .models import Course

def index(request):
    courses = Course.objects.find()
    context = {'courses': courses}

    return render(request, 'courses/index.html', context)

def course(request, slug):
    course = get_object_or_404(Course, slug = slug)
    context = {'course': course}

    return render(request, 'courses/course.html', context)
