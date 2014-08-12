from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from blog.models import Blog
import datetime
import khayyam
from dateutil import tz

########################################## login


def login_user(request):
    error = ""
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            
                login(request, user)
                return redirect('/cpanel/')
            
        else:
            error = "Your username and/or password were incorrect."

    return render(request,'login.html',{'state':error, 'username': username})


########################################## control panel


def cpanel(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    else:
        articles=[];
        counter=0;
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('Asia/Tehran')
        print to_zone
        for a in Blog.objects.all().order_by('-time'):
            articles.append({})
            utc = a.time.replace(tzinfo=from_zone)
            lcl = utc.astimezone(to_zone)
            jalali_now = khayyam.JalaliDatetime.from_datetime(lcl)
            articles[counter]['time']=jalali_now.strftime("%C")
            articles[counter]['title']=a.title
            articles[counter]['content']=a.content
            articles[counter]['id']=a.id
            counter+=1
        allnews = Blog.objects.all().order_by('-time')
        return render(request, 'cpanel.html',{'news':articles})


########################################## blog


def blog(request):
    articles=[];
    counter=0;
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Tehran')
    print to_zone
    for a in Blog.objects.all().order_by('-time'):
        articles.append({})
        print a.time
        utc = a.time.replace(tzinfo=from_zone)
        lcl = utc.astimezone(to_zone)
        print lcl
        jalali_now = khayyam.JalaliDatetime.from_datetime(lcl)
        articles[counter]['time']=jalali_now.strftime("%C")
        articles[counter]['title']=a.title
        articles[counter]['content']=a.content
        counter+=1
    allnews = Blog.objects.all().order_by('-time')
    return render(request, 'blog.html',{'news':articles})


########################################## logout href


def logout_view(request):
    logout(request)
    return redirect('/login/')


########################################## add news


def add_news(request):

    if not request.user.is_authenticated():
        
        return redirect('/login/')
    else:
        error = ""
        title = content = ""
        maybe_title=maybe_content=""

        if 'add_title' in request.POST and 'add_content' in request.POST: 
            add_title = request.POST.get('add_title')
            add_content = request.POST.get('add_content')
            if not add_content or not add_title:
                error = "please enter the form completely"
                maybe_title = request.POST.get('add_title')
                maybe_content = request.POST.get('add_content')
            else:
                print 'time'
                print datetime.datetime.now()
                p = Blog(title=add_title,content = add_content,time=datetime.datetime.now())
                p.save()
                return redirect('/cpanel/')

    return render(request, 'addnews.html', {'state':error,'maybe_title':maybe_title,'maybe_content':maybe_content})


########################################## edit news


def edit_news(request,number):

    if not request.user.is_authenticated():

        return redirect('/login/')

    else:
        error = ""
        number = int(number)
        p = Blog.objects.get(id = number)
        edit_title = p.title
        edit_content = p.content

        if 'form_title' in request.POST and 'form_content' in request.POST:
            get_title = request.POST.get('form_title')
            get_content = request.POST.get('form_content')
            if not get_title or not get_title:
                edit_title = get_title
                edit_content = get_content
                error = "please enter the form completely"
            else:
                p.title = get_title
                p.content = get_content
                p.save()
                return redirect('/cpanel/')


        return render(request, 'editnews.html', {'state':error ,'number':number ,'edit_title':edit_title , 'edit_content': edit_content})


########################################## delete news


def delete_news(request,number):

    if not request.user.is_authenticated():

        return redirect('/login/')

    else:

        number = int(number)
        p = Blog.objects.get(id = number)
        p.delete()
        return redirect('/cpanel/')
