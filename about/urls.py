"""TRIUMPH URL Configuration

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
from django.urls import path
from django.conf.urls import include
from . import views
# uk/
urlpatterns = [
    path('', views.index, name='index'),
    # path('contact-search/', views.about_search, name='about_search'),
    # path('payment-search/', views.about_search, name='about_search'),
    # path('reviews-search/', views.about_search, name='about_search'),
    # path('production-search/', views.about_search, name='about_search'),
    path('error_404/', views.about_search, name='about_search'),
    path('error_404/', views.about_search_mobile, name='about_search_mobile'),
    path('production/', include('production.urls')),
]