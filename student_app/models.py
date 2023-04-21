from django.db import models


class student_table(models.Model):
    student_name = models.CharField(max_length=20)
    date_of_birth=models.CharField(max_length=20)
    mark_of_physics=models.IntegerField()
    mark_of_maths=models.IntegerField()
    mark_of_chemistry=models.IntegerField()
    mark_of_computerscience=models.IntegerField()
    percentage=models.CharField(max_length=10)

# Create your models here.
