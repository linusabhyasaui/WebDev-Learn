from django.shortcuts import render
from django.http import HttpResponse

from .models import Lesson


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if not request:
        return render("down.html")

    return render(request, "lessons_home.html")


# TODO: input
def lesson_add(request):
    # return HttpResponse("Hello, world. You're at the lessons index.")
    all_lessons = 0
    all_lessons = Lesson.objects.all()

    if not all_lessons:
        return HttpResponse('')

    lesson_count = Lesson.objects.all().count()

    context = {'all_lessons': all_lessons}
    context = {'lesson_count': lesson_count}
    return render(request, "lessons_add.html", context)


# def contact(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = ContactForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             # Process the data in form.cleaned_data
#             # ...
#
#             print form.cleaned_data['my_form_field_name']
#
#             return HttpResponseRedirect('/thanks/') # Redirect after POST
#     else:
#         form = ContactForm() # An unbound form
#
#     return render_to_response('lessons_add.html', {
#         'form': form,
#     })

def lesson_view(request):
    all_lessons = 0
    all_lessons = Lesson.objects.all()

    if not all_lessons:
        return HttpResponse('')

    context = {'all_lessons': all_lessons}

    return render(request, "lessons_view.html", context)


def lesson_wipe(request):
    all_lessons = 0
    all_lessons = Lesson.objects.all()

    if not all_lessons:
        return HttpResponse('')

    lesson_count = Lesson.objects.all().count()

    context = {'all_lessons': all_lessons}
    context = {'lesson_count': lesson_count}
    # TODO: deletion
    Lesson.objects.filter(name=id).delete()

    return render(request, "lessons_delete.html", context)


def db(request):
    all_lessons = Lesson.objects.all()
    all_lessons.save()

    return render(request, "db.html", {"lessons": all_lessons})
