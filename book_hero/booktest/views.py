import hashlib
import json
import os
import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page

from book_hero import settings
from booktest.models import *

from django.core.paginator import Paginator
# Create your views here.


def index(request):
    print(request.path, request.encoding, request.method, request.COOKIES)
    return render(request, 'index.html', {'booklist': BookInfo.books.all()})


# def detail(request, id):
#     book = BookInfo.books.get(id=id)
#     print(book)
#     return render(request, 'booktest/detail.html', {'book': book})


def area(request, id):
    area = CityInfo.objects.get(id=id)
    return render(request, 'area.html', {'areas': area})


def get_test1(request):

    return render(request, 'get_test1.html')


def get_test2(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    context = {'a': a, 'b': b}
    print(context)
    return render(request, 'get_test2.html', context)


def get_test3(request):
    a = request.GET.getlist('a')
    b = request.GET.get('b')
    context = {'a': a, 'b': b}
    print(a)
    print(context)
    return render(request, 'get_test3.html', context)


def post_test1(request):
    return render(request, 'post_test1.html')


def post_test2(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    ugender = request.POST.get('ugender')
    # uhobby = request.POST.getlist('uhobby')
    uhobby = request.POST.get('uhobby')
    context = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby}
    return render(request, 'post_test2.html', context)


def index_rspn(request):
    print('---------------------------------------------------------**************************---------')
    response = HttpResponse()
    if request.COOKIES.get('h1'):
        response.write('<h1>' + request.COOKIES.get('h1') + '</h1>')
    # 最好使用英文，如果使用中文，会导致编码错误
    response.set_cookie('h1', 'hello', 120)
    print(request.COOKIES.get('h1'))
    response.write('hello,world')
    return response


def index2(request, id):
    print(id)
    return HttpResponseRedirect('js/')


def index_js(request):
    return HttpResponse('我是一个粉刷匠')


def index_json(request):
    return JsonResponse({'list': 'abc'})


def detail(request, id):
    try:
        book = get_object_or_404(BookInfo, pk=id)
    except BookInfo.MultipleObjectsReturned:
        book = None
    return render(request, 'detail.html', {'book': book})


def login(request):
    return render(request, 'login.html')


def home(request):

    return render(request, 'home.html')


def login_handle(request):
    if request.method == 'GET':
        print('---------------------')
    else:
        # resp = redirect('user/home')
        # request.session['uname'] = request.POST['uname']
        # return redirect(reversed('user:home'))
        user_name = request.POST.get('uname')
        verifycode = request.POST.get('verifycode')
        if verifycode.lower() == request.session['verifycode'].lower():
            print('------------------------------')
            f1 = request.FILES.get('pic')

            print(f1)

            # uploadFile = req.FILES.get('img')
            # saveFileName = newFileName(uploadFile.content_type)

            fname = os.path.join(settings.MEDIA_ROOT, newFileName(f1.content_type))

            print(fname)

            with open(fname, 'wb') as pic:
                for c in f1.chunks():
                    pic.write(c)

            return render(request, 'home.html', {'uname': user_name})

        else:
            return redirect('/user/login')


def logout(request):
    # request.session['uname'] = None
    # del request.session['uname']
    # request.session.clear()
    request.session.flush()
    return redirect('/user/home')


def newFileName(contentType):
    fileName = crypt(str(uuid.uuid4()))
    extName = '.jpg'
    if contentType == 'image/png':
        extName = '.png'

    return fileName + extName


def crypt(pwd, cryptName='md5'):
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    return md5.hexdigest()


def pag_test(request, p_index):
    print('------------------------------------------------')
    list1 = ProvInfo.objects.get_queryset()
    p = Paginator(list1, 10)
    if p_index == '':
        p_index = '1'

    p_index = int(p_index)
    list2 = p.page(p_index)
    plist = p.page_range
    return render(request, 'province.html', {'list': list2,
                                                      'plist': plist,
                                                      'p_index': p_index})


def image(request):

    return render(request, 'ddd.html')


def prov(request):
    return render(request, 'area_choice.html')


@cache_page(3600)
def prov_ajax(request):
    prov = {}
    provinces = ProvInfo.objects.all()
    for province in provinces:
        prov[province.id] = [province.provinceid, province.province]
    return JsonResponse(prov)


@cache_page(3600)
def city_ajax(request, id):
    city = {}
    cities = ProvInfo.objects.filter(provinceid=id).first().cityinfo_set.all().values()
    # for cit in cities:
    #     print(cit.get('cityid'))
    # city[cit.id] = [cit.get('cityid'), cit.get.('city')]

    for i in range(len(cities)):
        city[i] = [cities[i].get('cityid'), cities[i].get('city')]
    return JsonResponse(city)


@cache_page(3600)
def area_ajax(request, id):
    print(id)
    area = {}
    areas = CityInfo.objects.filter(cityid=id).first().areainfo_set.all().values()

    for i in range(len(areas)):
        area[i] = [areas[i].get('areaid'), areas[i].get('area')]
        print(area[i])
    return JsonResponse(area)


def editor(request):
    return render(request, 'editor.html')


def content(request):
    hname = request.POST.get('hname')
    hcontent = request.POST.get('hcontent')
    heroinfo = HeroInfo.heros.get(pk=1)
    heroinfo.hname = hname
    heroinfo.hcontent = hcontent
    heroinfo.save()

    return render(request, 'content.html', {'hero': heroinfo})














