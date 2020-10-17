from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=500)
    lecturer = models.CharField(max_length=500)
    sks = models.PositiveIntegerField()
    description = models.TextField()
    semester = models.CharField(max_length=500)
    room = models.CharField(max_length=500)

