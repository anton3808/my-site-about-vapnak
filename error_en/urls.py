from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error_404/', views.error_en_search, name='error_en_search'),
    path('error_404/', views.error_en_search_mobile, name='error_en_search_mobile'),
  #   path('production-search/', views.error_en_search, name='error_en_search'),
  #   path('contact-search/', views.error_en_search, name='error_en_search'),
  #   path('payment-search/', views.error_en_search, name='error_en_search'),
  #   path('reviews-search/', views.error_en_search, name='error_en_search'),
  #   path('error_404/', views.error_en_search, name='error_en_search'),



		# path('production-search/', views.error_en_search_mobile, name='error_en_search_mobile'),
  #   path('contact-search/', views.error_en_search_mobile, name='error_en_search_mobile'),
  #   path('payment-search/', views.error_en_search_mobile, name='error_en_search_mobile'),
  #   path('reviews-search/', views.error_en_search_mobile, name='error_en_search_mobile'),
  #   path('error_404/', views.error_en_search_mobile, name='error_en_search_mobile'),
]