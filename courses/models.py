from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=100)

    duration = models.CharField(max_length=50)

    department = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.name