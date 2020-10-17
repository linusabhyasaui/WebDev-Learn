from django.urls import path

from django.contrib import admin
import lessons.views

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

app_name = 'lessons'
urlpatterns = [
    path("", lessons.views.index, name="index"),
    path("delete_lesson", lessons.views.lesson_wipe, name="clear_lesson"),
    path("add_lesson", lessons.views.add_lesson, name="add_lesson"),
    path("view_lesson", lessons.views.lesson_view, name="view_lesson"),
    path("add", lessons.views.add, name="add"),
    path("delete", lessons.views.delete, name="delete"),
]
