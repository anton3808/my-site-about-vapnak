from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error_404/', views.error_ru_search, name='error_ru_search'),
    path('error_404/', views.error_ru_search_mobile, name='error_ru_search_mobile'),
]