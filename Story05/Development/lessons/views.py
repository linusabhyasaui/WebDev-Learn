from django.shortcuts import render
from django.http import HttpResponse

from .models import Lessons


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if not request:
        return render("down.html")

    return render(request, "lessons_home.html")


# TODO: input
def lesson_add(request):
    all_lessons = Lessons.objects.all()

    if not all_lessons:
        return HttpResponse('')

    lesson_count = Lessons.objects.all().count()

    context = {'all_lessons': all_lessons}
    context = {'lesson_count': lesson_count}
    return render(request, "lesson_add.html", context)


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
    all_lessons = Lessons.objects.all()

    if not all_lessons:
        return HttpResponse('')

    context = {'all_lessons': all_lessons}

    return render(request, "lesson_view.html", context)


def lesson_wipe(request):
    all_lessons = Lessons.objects.all()

    if not all_lessons:
        return HttpResponse('')

    lesson_count = Lessons.objects.all().count()

    context = {'all_lessons': all_lessons}
    context = {'lesson_count': lesson_count}
    # TODO: deletion
    Lessons.objects.filter(name=id).delete()

    return render(request, "lessons_delete.html", context)
