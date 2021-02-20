from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

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

@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2)
    page = request.GET.get("page")
    '''
        获取第 page 页的数据。如果当前没有页数，抛 PageNotAnInteger 异常，返回第一页的数据。如果超出最 大页数的范围，抛 EmptyPage 异常，返回最后一页面的数据。
    '''
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)
    return render(request,'guest_manage.html',{'user':username,'guests':contents})

@login_required
def sign_index(request,event_id):
    event = get_object_or_404(Event,id = event_id)
    return render(request,'sign_index.html',{'event':event})

@login_required
def sign_index_action(request,event_id):
    '''
    首先，查询 Guest 表判断用户输入的手机号是否存在，如果不存在将提示用户“手机号为空或不存在”。
    然后，通过手机和发布会 id 两个条件来查询 Guest 表，如果结果为空将提示用户“该用户未参加此次发布会。
    最后，再通过手机号查询 Guest 表，判断该手机号的签到状态是否为 1，如果为 1，表示已经签过到了， 返回用户“已签到”，
    否则，将提示用户“签到成功！”，并返回签到用户的信息。
    :param request:
    :param event_id:发布会id
    :return:
    '''
    event = get_object_or_404(Event, id=event_id)
    '''
    上面这句等同于：
    from django.http import Http404

    def my_view(request):
        try:
            obj = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            raise Http404("No MyModel matches the given query.")
    '''
    phone = request.POST.get('phone','')
    result = Guest.objects.filter(phone = phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': '手机号错误.'})
    result = Guest.objects.filter(phone=phone,event_id=event_id)
    print("结果是：",result)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': '发布会或者手机号错误.'})
    result = Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "该用户已签到过，不用重复签到."})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign = '1')
    return render(request, 'sign_index.html', {'event': event, 'hint':'签到成功!', 'guest': result})

@login_required
def search_phone(request):
    username = request.session.get('user','')
    search_phone = request.GET.get('phone','')
    page = request.GET.get('page')
    guest_list = Guest.objects.filter(phone__contains=search_phone)
    paginator = Paginator(guest_list,2)
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)
    return render(request,'guest_manage.html',{'user':username,'guests':contents})

@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/login/')
    return response