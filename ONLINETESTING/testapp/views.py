from django.db.models.fields import EmailField
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import User
from testapp.models import question
from testapp.models import register
from django.contrib.auth.hashers import make_password,check_password
import random

def authentication(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('http://localhost:8000/testapp/testpaper/')
        else:
            data['error']='username and password is incorrect'
            res=render(request,'testapp/login.html',data)
            return res
    else:
        s='Http://localhost:8000/testapp/loginpage/'
        return HttpResponseRedirect(s)
        

def loginpage(request):
    res=render(request,'testapp/login.html')
    return res

def registrationpage(request):
    res=render(request,'testapp/registration.html')
    return res

def addregistration(request):
    if request.method =='POST':
        
      #  if User.objects.get(username=request.POST['username']).username:
       #     warn={"warning":"username already exist"}
        #    res=render(request,"testapp/registration.html",warn)
         #   return res
        
        userobj=User()
        usernamee=request.POST['username'] 
        passwordd=make_password(request.POST['password'])
        fullnamee=request.POST['fullname']
        contactt=request.POST['contact']
        emaill=request.POST['email']
        addresss=request.POST['address']
        userobj.username=usernamee
        userobj.password=passwordd
        userobj.save()
        regobj=register()
        regobj.user=userobj
        regobj.fullname=fullnamee
        regobj.contact=contactt
        regobj.email=emaill
        regobj.address=addresss
        regobj.save()
        data={'fullname':fullnamee,'contact':contactt,'email':emaill,'address':addresss,"username":usernamee}
        res=render(request,'testapp/afterregistration.html',data)
        return res
        
    else:
        res=render(request,"testapp/login.html")
        return res
        

def testpaper(request):
    if request.session.has_key('username'):
        s=set()
        while(len(s)<5):
            s.add(random.randint(1,20))
        que=[]
        for index in s:
            que.append(question.objects.all()[index])
        data={'ques':que}
        res=render(request,'testapp/testpaper.html',data)
        return res
    else:
        res=HttpResponse('http://localhost:8000/testapp/loginpage/')
        return res
  
       

def answercheck(request):
    result=0
    if request.method=="POST":
        if request.POST['0option']==request.POST['0answer']: 
            result+=1
        if request.POST['1option']==request.POST['1answer']:
            result+=1
        if request.POST['2option']==request.POST['2answer']:
            result+=1
        if request.POST['3option']==request.POST['3answer']:
            result+=1
        if request.POST['4option']==request.POST['4answer']:
            result+=1
        a= (5-result)

        data={'marks':result,'check':10,'mate':10,'number':a}
        res=render(request,'testapp/resultpage.html/',data)
        return res
        ''' if request.POST['2']==request.POST['2answer']:
                result+=1
        if request.POST['3']==request.POST['3answer']:
                result+=1
        if request.POST['4']==request.POST['4answer']:
                result+=1
        if request.POST['5']==request.POST['5answer']:
                result+=1
        data={'marks': result}
        res=render(request,'testapp/resultpage.html',data)
        return res
    else:
      #  return HttpResponseRedirect("http://localhost:8000/testapp/loginpage/")
         return HttpResponse(1000)'''









        





