from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Monster,Marvel,Dccomics
from . forms import dcform,mcform,marvelform



# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def delete3(request,id):
    if request.method == "POST":

        movie=Dccomics.objects.get(id=id)
        movie.delete()
        # return redirect('irfanweb/')
    return render(request,'delete3.html')
def delete2(request,id):
    if request.method == "POST":
        movie=Monster.objects.get(id=id)
        movie.delete()
        # return redirect('irfanweb/')
    return render(request,'delete2.html')

def delete1(request,id):
    if request.method == "POST":

        movie=Marvel.objects.get(id=id)
        movie.delete()
        # return redirect('irfanweb/')
    return render(request,'delete1.html')





def update3(request,id):
    macc=Marvel.objects.get(id=id)
    forms=marvelform(request.POST or None,request.FILES,instance=macc)
    if forms.is_valid():
        forms.save()
    return render(request,'update3.html',{'forms':forms,'macc':macc})
def update2(request,id):
    mcc=Monster.objects.get(id=id)
    forms=mcform(request.POST or None,request.FILES,instance=mcc)
    if forms.is_valid():
        forms.save()
    return render(request,'update2.html',{'forms':forms,'mcc':mcc})
def update1(request,id):
    dcc=Dccomics.objects.get(id=id)
    forms=dcform(request.POST or None,request.FILES,instance=dcc)
    if forms.is_valid():
        forms.save()
        # return redirect('irfanwebs')
    return render(request,'update1.html',{'forms':forms,'dcc':dcc})



def add2(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        year = request.POST.get('year')
        cast = request.POST.get('cast')
        category = request.POST.get('category')
        movie=Monster(name=name,desc=desc,img=img,year=year,cast=cast,category=category)
        movie.save()
        # return redirect('irfanweb/')
    return render(request,'add2.html')
def add1(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        year = request.POST.get('year')
        cast = request.POST.get('cast')
        category = request.POST.get('category')
        movie=Dccomics(name=name,desc=desc,img=img,year=year,cast=cast,category=category)
        movie.save()
        # return redirect('irfanweb/')
    return render(request,'add1.html')
def add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        year = request.POST.get('year')
        cast = request.POST.get('cast')
        category = request.POST.get('category')
        movie=Marvel(name=name,desc=desc,img=img,year=year,cast=cast,category=category)
        movie.save()
        # return redirect('irfanweb/')
    return render(request,'add.html')
def detail2(request,monster_id):
    monster=Monster.objects.get(id=monster_id)
    return render(request,'detail2.html',{'monster':monster})
def irfanwebss(request):
    moster=Monster.objects.all()
    return render(request,'irfanwebss.html',{'monster':moster})
def detail1(request,dc_id):
    dcc=Dccomics.objects.get(id=dc_id)
    return render(request,'detail1.html',{'dcc':dcc})
def irfanwebs(request):
    dc=Dccomics.objects.all()
    return render(request,'irfanwebs.html',{'dc':dc})
def detail(request,marvel_id):
    movie=Marvel.objects.get(id=marvel_id)
    return render(request,'detail.html',{'movie':movie})

def irfanweb(request):
    marvel=Marvel.objects.all()
    return render(request,'irfanweb.html',{'marvel':marvel})
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        userr=auth.authenticate(username=username,password=password)

        if userr is not None:
            auth.login(request,userr)
            messages.info(request,'User created Successfully')
            return redirect('irfanweb/')

        else:
            messages.info(request,'Invalid Password or Username')

    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if cpassword==password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username has already taken")
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email has already taken")
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                messages.info(request,'User Created')
                return redirect('login.')

        else:
            messages.info(request,"password doesnt match")



    return render(request,'register.html')

