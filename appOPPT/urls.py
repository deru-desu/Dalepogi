from django.urls import path
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('registeradmin/', views.registerPage, name="registerpage"),
    path('searchadmin/', views.searchadmin, name='searchadmin'),
    path('readadmin/', views.listadmin, name='readadmin'),

    path('registration/', views.registration, name='registration'),
    path('read/', views.list, name='read'),
    path('update/<int:pk>/', views.UpdateInfo, name='update'),
    path('search/', views.search, name='search'),


    #url(r'edit/(?P<id>\d+)$', views.edit, name='edit'),
    #url(r'edit/update/(?P<id>\d+)$', views.update, name='update'),
    #url(r'delete/(?P<id>\d+)$', views.delete, name='delete'),
]