from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('error_404/', views.production_ru_search_mobile, name='production_ru_search_mobile'),
  path('processing_4/', views.send_email_4_ru, name='email_4_ru'),
  path('processing_3/', views.send_email_3_ru, name='email_3_ru'),
  path('processing_2/', views.send_email_2_ru, name='email_2_ru'),
  path('processing_1/', views.send_email_1_ru, name='email_1_ru'),
]