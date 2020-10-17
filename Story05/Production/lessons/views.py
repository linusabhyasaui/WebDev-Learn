from django.shortcuts import render
from django.http import HttpResponse

from .models import Lessons


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "lessons_home.html")


# TODO:
def lesson_add(request):
    all_lessons = Lessons.objects.all()
    lesson_count = Lessons.objects.all().count()

    context = {'all_lessons': all_lessons}
    context = {'lesson_count': lesson_count}
    return render(request, "lesson_add.html")


def lesson_view(request):
    all_lessons = Lessons.objects.all()

    context = {'all_lessons': all_lessons}

    if not all_lessons:
        return HttpResponse('')

    return render(request, "lesson_view.html", context)
