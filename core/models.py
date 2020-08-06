from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):

    department = models.CharField(max_length=4,default='LATN')
    course_number = models.PositiveSmallIntegerField(default=000)

    semester_options = [
        ('f', 'fall'),
        ('s', 'spring')
    ]

    semester = models.CharField(
        max_length = 1,
        choices = semester_options,
        default = 'f'
    )

    year = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    course = models.ForeignKey(
        Course,
        related_name = 'students',
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.user.username
