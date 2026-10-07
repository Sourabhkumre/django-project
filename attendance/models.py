from django.db import models


class Attendance(models.Model):

    student_name = models.CharField(max_length=100)

    subject = models.CharField(max_length=100)

    date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
        ]
    )

    def __str__(self):
        return self.student_name