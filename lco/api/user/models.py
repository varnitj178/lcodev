from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50,default='Anonymous')
    email = models.EmailField(max_length=250,unique=True)

    username = None
    # the user name is now governed by the email as a login credential
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=50,blank= True,null = True)

    gender = models.CharField(max_length=10,blank= True,null = True)

    # django does not work on the session token but we need and we are making
    # it as a dafault as we are checking the value 0 if user in not signed in
    #and restricting the length of token to 10 length
    session_token = models.CharField(max_length=10,default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

