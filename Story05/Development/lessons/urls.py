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

urlpatterns = [
    path("", lessons.views.index, name="index"),
    path("clear", lessons.views.lesson_wipe, name="wipe"),
    path("add", lessons.views.lesson_add, name="add"),
    path("view", lessons.views.lesson_view, name="view"),
]
