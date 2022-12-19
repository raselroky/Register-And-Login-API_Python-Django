from . models import Register
from django.forms import fields
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','email','firstname','lastname','mobile','password','retype_password']
