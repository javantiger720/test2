# _*_ coding:utf-8 _*_
from django.shortcuts import render, redirect
from datetime import timedelta
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.conf import settings
import os
from django.core.paginator import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache


# Create your views here.

def index(request):
    values = BookInfo.book1.values()
    return HttpResponse('hello 你好！=={}'.format(values))


def get_test1(request):
    return render(request, 'booktest/get_test1.html')


def get_test2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a': a1, 'b': b1, 'c': c1}
    return render(request, 'booktest/get_test2.html', context)


def get_test3(request):
    a = request.GET.getlist('a')
    b = request.GET['b']
    context = {'a': a, 'b': b}
    return render(request, 'booktest/get_test3.html', context)


def post_test1(request):
    return render(request, 'booktest/post_test1.html')


def post_test2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby}
    return render(request, 'booktest/post_test2.html', context)


def cookie_test(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if 'h1' in cookie.keys():
        response.write(cookie['h1'])
    # response.set_cookie('h1', 'abc')
    return response


def redirect_test1(request):
    return redirect('/booktest/redirect_test2')


def redirect_test2(request):
    return JsonResponse({'这是重定向后的页面': '是的'})


def session1(request):
    uname = request.session.get('my_name', '未登录')
    context = {'uname': uname}
    return render(request, 'booktest/session1.html', context)


def session2(request):
    return render(request, 'booktest/session2.html')


def session2_handle(request):
    uname = request.POST['uname']
    request.session['my_name'] = uname
    request.session.set_expiry(None)  # 设置session的过期时间，0：关闭浏览器过期，整数：整数秒后过期，None：永不过期，timedalte：指定时间差后过期
    return redirect('/booktest/session1/')


def session3(request):
    del request.session['my_name']
    return redirect('/booktest/session1/')


def static_file_test(request):
    return render(request, 'booktest/static_file_test.html')


def upload_pic(request):
    return render(request, 'booktest/upload_pic.html')


def upload_pic2(request):
    pic = request.FILES['pic1']
    picname = os.path.join(settings.MEDIA_ROOT, pic.name)
    with open(picname, 'wb+') as pic1:
        for c in pic.chunks():
            pic1.write(c)
    return HttpResponse('<img src="/booktest/static/media/{}"/>'.format(pic.name))


def herolist(request, pagenum):
    if pagenum == '':
        pagenum = 1
    heros = HeroInfo.objects.all()
    paginator = Paginator(heros, 5)
    page = paginator.page(int(pagenum))
    context = {'page': page}
    return render(request, 'booktest/herolist.html', context)


def area(request):
    return render(request, 'booktest/area.html')


def pro(request):
    data = AreaInfo.objects.filter(parea__isnull=True)
    lst = []
    for item in data:
        lst.append([item.id, item.title])
    return JsonResponse({'data': lst})


def city(request, pro_id):
    city_data = AreaInfo.objects.filter(parea_id=pro_id)
    lst = []
    for item in city_data:
        lst.append({'id': item.id, 'title': item.title})
    return JsonResponse({'data': lst})


def district(request, city_id):
    city_data = AreaInfo.objects.filter(parea_id=city_id)
    lst = []
    for item in city_data:
        lst.append({'id': item.id, 'title': item.title})
    return JsonResponse({'data': lst})


def html_editor(request):
    return render(request, 'booktest/html_editor.html')


# @cache_page(60 * 10)
def cache_test1(request):
    # return HttpResponse("hello cache")
    # return render(request, 'booktest/cache1.html')
    # cache.set('key1', 'value1', 600)
    cache.clear()
    return HttpResponse('ok')
