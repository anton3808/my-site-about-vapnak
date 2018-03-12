from django.urls import path
from .import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('error_404/', views.production_en_search_mobile, name='production_en_search_mobile'),
  path('processing_4/', views.send_email_4, name='email_4_en'),
  path('processing_3/', views.send_email_3, name='email_3_en'),
  path('processing_2/', views.send_email_2, name='email_2_en'),
  path('processing_1/', views.send_email_1, name='email_1_en'),
]