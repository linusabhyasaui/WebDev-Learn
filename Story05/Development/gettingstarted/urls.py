from django.urls import path, include

from django.contrib import admin
import lessons.views
import hello.views

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
    path("/clear", lessons.views.lesson_wipe, name="wipe"),
    path("schedule/", lessons.views.lesson_add, name="add"),
    path("schedule/add", lessons.views.lesson_add, name="add"),
    path("schedule/view", lessons.views.lesson_view, name="view"),

    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
