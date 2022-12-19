
from myapp import views
from django.urls import path,include


urlpatterns = [
    path('register/',views.RegisterApi),
    path('login/',views.LoginApi),

]