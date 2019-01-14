from django.urls import path, re_path
from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'get_test1/', views.get_test1, name='get_test1'),
    path(r'get_test2/', views.get_test2, name='get_test2'),
    path(r'get_test3/', views.get_test3, name='get_test3'),

    path(r'post_test1/', views.post_test1, name='post_test1'),
    path(r'post_test2/', views.post_test2, name='post_test2'),

    path(r'cookie_test/', views.cookie_test, name='cookie_test'),

    path(r'redirect_test1/', views.redirect_test1, name='redirect_test1'),
    path(r'redirect_test2/', views.redirect_test2, name='redirect_test2'),

    path(r'session1/', views.session1, name='session1'),
    path(r'session2/', views.session2, name='session2'),
    path(r'session2_handle/', views.session2_handle, name='session2_handle'),
    path(r'session3/', views.session3, name='session3'),

    path(r'static_file_test/', views.static_file_test, name='static_file_test'),

    path(r'upload_pic/', views.upload_pic, name='upload_pic'),
    path(r'upload_pic2/', views.upload_pic2, name='upload_pic2'),

    re_path(r'herolist/(\d*)/', views.herolist, name='herolist'),

    path(r'area/', views.area, name='area'),
    path(r'pro/', views.pro, name='pro'),
    re_path(r'city/(\d+)/', views.city, name='city'),
    re_path(r'district/(\d+)/', views.district, name='district'),

    path(r'html_editor/', views.html_editor, name='html_editor'),

    path(r'cache_test1/', views.cache_test1, name='cache_test1'),

]

















