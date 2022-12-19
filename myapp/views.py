from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from . models import Register
from . serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from . import serializers


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
    
    if (Register.objects.filter(username=username).exists()):
        return Response({"Message":"This username is already taken,try Another!"})
    if(len(str(password))<6 and len(str(retype_password))<6):
        return Response({"Message":"Password Too short! try Again."})
    if(password!=retype_password):
        return Response({"Message":"Two password didn't matched ,try agian!"})
    
    user=Register(username=username,email=email,firstname=firstname,lastname=lastname,mobile=mobile,password=password,retype_password=retype_password)
    user.save()
    return Response({'username':username,'email':email,'firstname':firstname,'lastname':lastname,'mobile':mobile,'password':password,'retype_password':retype_password})

    #return render(request, 'signup.html', {'user':user})

@api_view(['GET','POST']) 
def LoginApi(request):
    if request.method=='POST':
        username=request.data['username']
        password=request.data['password']

    username1=Register.objects.filter(username=username,password=password).exists()
    password1=Register.objects.filter(password=password,username=username).exists()
    print(username1,password1)
    if(username1 and password1):
        return Response({"Message":"Successfully Login!"})
    else:
        return Response({"Message":"Error, complete your registration then try login."})
    
