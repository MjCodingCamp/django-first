from django.db import models


class UserProfile(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=18)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )
    about = models.TextField(blank=True)

