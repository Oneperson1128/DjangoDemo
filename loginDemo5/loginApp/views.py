from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from loginApp.models import Event, Guest


def login(request):
    return render(request, "login.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        #接受2个参数，用户名 密码，在用户名密码正确的情况下返回一个user对象。如果不正确，返回None
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, "login.html", {'error': '用户名或者密码错误'})

        '''
        if username == "admin" and password == 'admin':
            # return HttpResponse("登录成功")
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request,"login.html",{'error':'用户名或者密码错误'})
        '''


@login_required
def event_manage(request):
    # return render(request, 'event_manage.html')
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username,'events':event_list})


@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,'event_manage.html',{'user':username,'events':event_list})

@login_required()
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request,'guest_manage.html',{'user':username,'guests':guest_list})