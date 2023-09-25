from django.db import models

class Lesson (models.Model):
    lesson_name = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    length_time = models.IntegerField()
class Product (models.Model):
    Product_name = models.CharField(max_length=30)
    Autor_name = models.CharField(max_length=30)
    lessons = models.ManyToManyField(Lesson)


