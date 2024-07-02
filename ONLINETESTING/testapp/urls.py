from django.urls import path
from testapp.views import *

urlpatterns=[
    path('authentication/',authentication),
    path('testpaper/',testpaper),
    path('loginpage/',loginpage),
    path('registrationpage/',registrationpage),
    path('addregistration/',addregistration),
    path('answercheck/',answercheck),
    
]