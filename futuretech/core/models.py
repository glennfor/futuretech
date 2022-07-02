from django.db import models
from django.forms import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


# Create your models here.

class RegisteredUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
   
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


    first_name  = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True)
    last_name   = models.CharField(max_length=20)
    birth_date  = models.DateField()
    gender      = models.CharField(max_length=3, choices=GENDER_CHOICES)
    email        = models.EmailField()
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    courses      = models.CharField(max_length=100, default='No Course Chosen')
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_fee = models.CharField(max_length=100, default='')
    registration_status = models.BooleanField(null=True)

    def get_course_list(self):
        return self.courses.split('\n')


   