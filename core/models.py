from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Course(models.Model):
#
#     department = models.CharField(max_length=4,default='LATN')
#     course_number = models.PositiveSmallIntegerField(default=000)
#
#     semester_options = [
#         ('f', 'fall'),
#         ('s', 'spring')
#     ]
#
#     semester = models.CharField(
#         max_length = 1,
#         choices = semester_options,
#         default = 'f'
#     )
#
#     year = models.PositiveSmallIntegerField()
#     title = models.CharField(max_length=256)
#
#     def __str__(self):
#         return self.title
#
# class Profile(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     course = models.ForeignKey(
#         Course,
#         related_name = 'course',
#         on_delete = models.CASCADE
#     )
#
#     def __str__(self):
#         return self.user.username

class UserCourse(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    course_choices = (
        ('CLAS199', 'Intro to Greco-Roman Gender and Sexuality'),
        ('LATN213', 'Intermediate Latin 1'),
        ('LATN399', 'Roman Constructions of Gender and Sexuality'),
    )

    course = models.CharField(
        max_length=256,
        choices=course_choices,
    )

    def __str__(self):
        return self.user.username
