from django.urls import path
from .import views 

urlpatterns = [
	path('', views.index, name='index'),
  path('processing_4/', views.send_email_4, name='email_4'),
  path('processing_3/', views.send_email_3, name='email_3'),
  path('processing_2/', views.send_email_2, name='email_2'),
  path('processing_1/', views.send_email_1, name='email_1'),
 
  path('error_404/', views.production_search_mobile, name='production_search_mobile'),
]