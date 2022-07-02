from django.db import models
from django.forms import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


# Create your models here.

class RegisteredUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N/A', 'Prefer Not To Say')
    )
    COURSE_CHOICES = (
        ('G', 'Game Development'),
        ('WD', 'Web Development'),
        ('MAD', 'Mobile App development'),
        ('R', 'Robotics'),
        ('GD', 'Graphics Design'),
        ('CM', 'Computer Maintenanace')
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


    first_name  = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True)
    last_name   = models.CharField(max_length=20)

    birth_date  = models.DateField()
    gender      = models.CharField(max_length=3, choices=GENDER_CHOICES)

    email        = models.EmailField()

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 

    course       = models.CharField(max_length=3, choices=COURSE_CHOICES)

    user         = models.OneToOneField(User, on_delete=models.CASCADE)
   