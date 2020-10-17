from django.urls import path, include

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

    path("schedule/", include('lessons.urls'), name="schedule"),

    path("db/", lessons.views.db, name="db"),
    path("admin/", admin.site.urls),
]
