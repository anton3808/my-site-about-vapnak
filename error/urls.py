from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error_404/', views.error_search, name='error_search'),
    path('error_404/', views.error_search_mobile, name='error_search_mobile'),
    path('../../../ru/error_404/', views.russian_language, name='russian_language'),
]