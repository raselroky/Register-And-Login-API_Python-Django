from django.db import models


class Register(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    mobile=models.CharField(max_length=11)
    password=models.CharField(max_length=100)
    retype_password=models.CharField(max_length=100)


    def __str__(self):
        return self.username
    
