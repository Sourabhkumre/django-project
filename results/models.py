from django.db import models


class Result(models.Model):

    student_name = models.CharField(max_length=100)

    subject = models.CharField(max_length=100)

    marks = models.IntegerField()

    total_marks = models.IntegerField(default=100)

    semester = models.IntegerField()

    def __str__(self):
        return self.student_name