from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from . models import Register
from . serializers import RegisterSerializer
from rest_framework.permissions import AllowAny


@api_view(['GET','POST'])

def RegisterApi(request):
    if request.method=='POST':
        username=request.data['username']
        email=request.data['email']
        firstname=request.data['firstname']
        lastname=request.data['lastname']
        mobile=request.data['mobile']
        password=request.data['password']
        retype_password=request.data['retype_password']
    
    if Register.objects.filter(username=username).exists():
        return Response({"Message":"This username is already taken,try Another!"})
    
    if password!=retype_password:
        return Response({"Message":"Two password didn't matched ,try agian!"})
    
    user=Register(username=username,email=email,firstname=firstname,lastname=lastname,mobile=mobile,password=password,retype_password=retype_password)
    user.save()
    return Response({'username':username,'email':email,'firstname':firstname,'lastname':lastname,'mobile':mobile,'password':password,'retype_password':retype_password})
    
