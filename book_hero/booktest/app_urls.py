"""book_hero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from booktest import views, views_utile

app_name = 'booktest'  # 将命名空间放在这里便解决了问题

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<id>\d+)$', views.detail, name='detail'),
    re_path(r'^area/(?P<id>\d+)$', views.area, name='area'),
    re_path(r'^index/(\d+)$', views.detail),
    re_path(r'^get_test1$', views.get_test1),
    re_path(r'^get_test2/$', views.get_test2),
    re_path(r'^get_test3/$', views.get_test3),
    re_path(r'^post_test1$', views.post_test1),
    re_path(r'^post_test2', views.post_test2),
    re_path(r'^index$', views.index_rspn),
    re_path(r'^index2/([0-9]+)$', views.index2),
    re_path(r'^index2/js/$', views.index_js),
    re_path(r'^index_json$', views.index_json),
    # url(r'^lists/(?P<table>\w+)/$', echo.views.lists, name='lists'),

    re_path(r'^home$', views.home, name='home'),
    re_path(r'^login$', views.login, name='login'),
    re_path(r'^login_handle$', views.login_handle, name='login_handle'),
    re_path(r'^logout$', views.logout, name='logout'),

    re_path(r'^verifycode$', views_utile.verifycode, name='verifycode'),

    re_path(r'^pag(?P<p_index>\d+)/$', views.pag_test, name='pag_test'),

    re_path(r'^image$', views.image, name='image'),

    re_path(r'^prov_ajax$', views.prov_ajax, name='prov_ajax'),

    re_path(r'^prov$', views.prov, name='prov'),
    re_path(r'^city_ajax/(?P<id>\d+)$', views.city_ajax, name='city_ajax'),
    re_path(r'^area_ajax/(?P<id>\d+)$', views.area_ajax, name='area_ajax'),

    re_path(r'^editor$', views.editor, name='editor'),
    re_path(r'^content$', views.content, name='content'),
]

