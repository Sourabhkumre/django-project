from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    course = models.CharField(max_length=100)

    semester = models.IntegerField()

    roll_number = models.CharField(max_length=20)

    admission_date = models.DateField()

    def __str__(self):
        return self.name