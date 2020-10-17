from random import randint

from django.db import models
from django.http import request
from django.shortcuts import get_object_or_404, redirect


class Lesson(models.Model):
    name = models.CharField(max_length=500)
    lecturer = models.CharField(max_length=40)
    sks = models.IntegerField(default=0)
    description = models.TextField()
    semester = models.CharField(max_length=9)
    room = models.CharField(max_length=20)

    def delete(self):
        self.delete()

    def __str__(self):
        return self.name
