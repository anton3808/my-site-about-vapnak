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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),


    
    path('', include('about.urls')),
    path('services/', include('services.urls')),
    path('production/', include('production.urls')),
    path('reviews/', include('reviews.urls')),
    path('contact/', include('contact.urls')),



    path('ru/', include('about_ru.urls')),
    path('ru/services/', include('services_ru.urls')),
    path('ru/production/', include('production_ru.urls')),
    path('ru/reviews/', include('reviews_ru.urls')),
    path('ru/contact/', include('contact_ru.urls')),



    path('en/', include('about_en.urls')),
    path('en/services/', include('services_en.urls')),
    path('en/production/', include('production_en.urls')),
    path('en/reviews/', include('reviews_en.urls')),
    path('en/contact/', include('contact_en.urls')),


    path('error_404/', include('error.urls')),
    path('ru/error_404/', include('error_ru.urls')),
    path('en/error_404/', include('error_en.urls')),
]
