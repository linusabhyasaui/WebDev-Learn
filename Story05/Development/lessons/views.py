from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .models import Lesson


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if not request:
        return render("down.html")

    return render(request, "lessons_home.html")


def add_lesson(request):
    try:
        all_lessons = Lesson.objects.all()
        flag = all_lessons.get(0).DoesNotExist
    except Exception as e:
        return render(request, "lessons_add_new.html")

    lesson_count = Lesson.objects.all().count()
    context = {'all_lessons': all_lessons, 'lesson_count': lesson_count}
    return render(request, "lessons_add.html", context)


def lesson_view(request):
    try:
        all_lessons = Lesson.objects.all()
    except not all_lessons.exists():
        raise Http404("Question does not exist")

    context = {'all_lessons': all_lessons}

    return render(request, "lessons_view.html", context)


def lesson_wipe(request):
    try:
        all_lessons = Lesson.objects.all()
    except not all_lessons.exists():
        raise Http404("Question does not exist")

    lesson_count = Lesson.objects.all().count()
    context = {'all_lessons': all_lessons, 'lesson_count': lesson_count}
    return render(request, "lessons_delete.html", context)


def db(request):
    all_lessons = Lesson.objects.all()
    all_lessons.save()
    return render(request, "db.html", {"lessons": all_lessons})


def add(request):
    the_values = {
        "key": "the_values"
    }
    for key, value in request.POST.items():
        the_values[key] = value

    new_lesson = Lesson(name=the_values["lesson"], lecturer=the_values["lecturer"],
                        description=the_values["description"], sks=the_values["credits"], room=the_values["room"],
                        semester=the_values["semester"])

    new_lesson.save()
    return redirect('lessons:view_lesson')


def delete(request):
    name = request.POST.get("name")
    lessons = Lesson.objects.all()
    lesson = lessons.filter(name=name)
    lesson.delete()
    return redirect('lessons:view_lesson')
